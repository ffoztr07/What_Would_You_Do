import base64
import os,json
from google import genai
from google.genai import types
from config import validate_api_key



def generate(question: str, user_answer: str):
    # Validate API key when function is called
    api_key = validate_api_key()
    client = genai.Client(
        api_key=api_key,
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"Question: {question}\nAnswer: {user_answer}"),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_LOW_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_ONLY_HIGH",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_LOW_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_NONE",
            ),
        ],
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            properties={
                "corrected_version_of_answer": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "rating": genai.types.Schema(
                    type=genai.types.Type.INTEGER,
                ),
            },
        ),
        system_instruction="""You are a grammar and content evaluation expert.
A client provides answers to given questions.
Your task is to:

Analyze the compatibility between each question and its corresponding answer.

Check the grammatical accuracy of the answer.

Scoring Criteria:

If the answer is both grammatically correct and fully compatible with the question → Score: 5 points (maximum).

If the answer is grammatically correct but not fully compatible → Score: 3–4 points.

If the answer is compatible but has grammar issues → Score: 2–3 points.

If the answer is neither grammatically correct nor relevant → Score: 0–1 point.
""",
    )

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        if not response.text:
            return {
                "corrected_version_of_answer": "No response received from the model",
                "rating": 0
            }
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            return {
                "corrected_version_of_answer": "Error processing model response",
                "rating": 0
            }
    except Exception as e:
        return {
            "corrected_version_of_answer": f"Error: {str(e)}",
            "rating": 0
        }

