import json
from ai_quiz import generate_questions

questions = generate_questions("Python", "beginner", 5)

print(json.dumps(questions, indent=4))