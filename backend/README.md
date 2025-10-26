# Alpha Mini Backend

A FastAPI backend for a question-answer evaluation system using Google's Gemini AI.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Variables
Make sure your `.env` file contains:
```
GEMINI_API_KEY=your_actual_api_key_here
```

The system will automatically load this from your `.env` file.

### 3. Initialize Database
```bash
python seed_questions.py
```

### 4. Run the Server
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /api/get_question` - Get a random question
- `POST /api/submit_answer` - Submit an answer for evaluation

## Features

- ✅ SQLModel database with SQLite
- ✅ 100+ realistic social situation questions
- ✅ Google Gemini AI integration for answer evaluation
- ✅ Grammar and content scoring
- ✅ Modern FastAPI with lifespan events
