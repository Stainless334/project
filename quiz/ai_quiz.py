import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()



client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

def generate_questions(topic, level, number):
    prompt = f"""
    Generate exactly {number} multiple-choice quiz questions
    about {topic} at the {level} difficulty level.

    Return ONLY a valid JSON array.
    Each question must have these keys:
    - "Quest": the question text
    - "Option": a list of exactly four answer options
    - "Ans": the correct answer, matching one of the options

    Example structure:
    [
        {{
            "Quest": "What does print() do in Python?",
            "Option": [
                "Displays output",
                "Creates a loop",
                "Defines a class",
                "Imports a module"
            ],
            "Ans": "Displays output"
        }}
    ]
    """

    response = client.chat.completions.create(
        model="cutycat2000x/MeowGPT-2.5",
        messages=[
            {
                "role": "system",
                "content": "You generate accurate multiple-choice quiz questions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content
    questions = json.loads(content)

    return questions
