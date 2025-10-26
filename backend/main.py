from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from llm import generate
from config import validate_api_key
import random
from pydantic import ValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from models import (
    Question, Answer, AnswerRequest, AnswerResponse, 
    QuestionResponse, get_session, init_db
)

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)

# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Validate API key and initialize database
    try:
        validate_api_key()
        
    except ValueError as e:
        print(f"❌ API key validation failed: {e}")
        raise e
    
    init_db()
    yield
    # Shutdown: Clean up resources (if needed)
    # For now, nothing to clean up

app = FastAPI(lifespan=lifespan)

# Add rate limiter state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://whatwouldyoudo.info",
        "https://www.whatwouldyoudo.info",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid input data", "errors": exc.errors()}
    )

@app.get("/api/get_question")
@limiter.limit("30/minute")  # Allow 30 questions per minute per IP
async def get_question(request: Request, session: Session = Depends(get_session)):
    # Get a random question from database
    questions = session.exec(select(Question)).all()
    if questions:
        question = random.choice(questions)
        return {"message": question.text}
    else:
        return {"message": "No questions available"}

@app.post("/api/submit_answer")
@limiter.limit("10/minute")  # Allow 10 submissions per minute per IP
async def submit_answer(
    request: Request,
    answer_request: AnswerRequest, 
    session: Session = Depends(get_session)
):
    try:
        response = generate(answer_request.question, answer_request.answer)
        
        # Get corrected answer and rating from response
        corrected_answer = response["corrected_version_of_answer"]
        rating = response["rating"]
        
        # Find the question in database
        question = session.exec(
            select(Question).where(Question.text == answer_request.question)
        ).first()
        
        if not question:
            # Create a new question if it doesn't exist
            question = Question(text=answer_request.question)
            session.add(question)
            session.commit()
            session.refresh(question)
        
        # Save answer to database
        answer = Answer(
            question_id=question.id,
            user_answer=answer_request.answer,
            corrected_answer=corrected_answer,
            rating=rating
        )
        session.add(answer)
        session.commit()
        session.refresh(answer)

        return {"corrected_answer": corrected_answer, "rating": round(rating, 1)}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


