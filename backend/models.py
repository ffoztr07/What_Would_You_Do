from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from datetime import datetime
from pydantic import validator
import re,os
from dotenv import load_dotenv

load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

# Question Model
class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field(index=True, max_length=500)
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Answer Model  
class Answer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    user_answer: str = Field(max_length=1000)
    corrected_answer: str = Field(max_length=1000)
    rating: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

# API Request/Response Models
class AnswerRequest(SQLModel):
    answer: str = Field(..., min_length=1, max_length=1000)
    question: str = Field(..., min_length=1, max_length=500)
    
    @validator('answer', 'question')
    def validate_content(cls, v):
        # Remove potentially dangerous characters and patterns
        dangerous_patterns = [
            '<script', '</script>', 'javascript:', 'onload=', 'onerror=',
            'DROP TABLE', 'DELETE FROM', 'INSERT INTO', 'UPDATE ',
            'UNION SELECT', '--', '/*', '*/', 'xp_', 'sp_'
        ]
        
        v_lower = v.lower()
        for pattern in dangerous_patterns:
            if pattern.lower() in v_lower:
                raise ValueError(f"Invalid content detected: {pattern}")
        
        # Remove HTML tags
        v = re.sub(r'<[^>]+>', '', v)
        
        # Remove extra whitespace
        v = ' '.join(v.split())
        
        return v

class AnswerResponse(SQLModel):
    corrected_answer: str
    rating: float

class QuestionResponse(SQLModel):
    message: str

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Database dependency
def get_session():
    with Session(engine) as session:
        yield session

# Initialize database (without sample questions - use seed script instead)
def init_db():
    create_db_and_tables()
