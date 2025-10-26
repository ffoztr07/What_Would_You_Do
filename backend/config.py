import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_api_key():
    """Validate that the API key is present"""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable is required. Please set it in your .env file.")
    return GEMINI_API_KEY
