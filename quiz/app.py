from flask import Flask, render_template, request, session, redirect, url_for, flash
from ai_quiz import generate_questions

app = Flask(__name__)
app.secret_key = "the secret flash"

@app.route("/", methods=['GET'])
def home():
    
    
    return render_template("index.html")

@app.route("/quiz", methods=['GET', 'POST'])
def quest():
    message = ""

    if request.method == 'GET':

        topic = request.args.get('topic')
        level = request.args.get('level')
        number = request.args.get('number')

        # Validate the topic and difficulty
        if not topic or not level:
            flash("Please select a topic and difficulty level.")
            return redirect(url_for("home"))

        # Validate the number of questions
        try:
            number = int(number)
        except (ValueError, TypeError):
            flash("Please enter a valid number.")
            return redirect(url_for("home"))

        if number > 25 or number < 5:
            flash("Please enter a number between 5 and 25.")
            return redirect(url_for("home"))

        # Generate questions using AI
        try:
            questions = generate_questions(topic, level, number)

            # Check that the AI returned the expected number
            if not isinstance(questions, list) or len(questions) != number:
                raise ValueError("The AI returned an unexpected number of questions.")

            # Save the quiz data
            session["questions"] = questions
            session["current_question"] = 0
            session["answers"] = {}

        except Exception as error:
            print(f"Question generation failed: {error}")
            flash("Unable to generate questions. Please try again.")
            return redirect(url_for("home"))

    elif request.method == 'POST':

        select = request.form.get('action')

        if select == 'previous':
            if session["current_question"] > 0:        
                session["current_question"] -= 1

        elif select == 'next':
            action = request.form.get('option')
            session["answers"][str(session["current_question"])] = action

            if session["current_question"] != len(session["questions"]) - 1:
                session["current_question"] += 1

        elif select == 'submit':
            action = request.form.get('option')
            session["answers"][str(session["current_question"])] = action
            score = 0

            for goal in session["answers"]:
                if session["answers"][goal] == session["questions"][int(goal)]["Ans"]:
                    score += 1
            session["score"] = score
            return redirect(url_for("result"))
    final = session["current_question"] == len(session["questions"]) - 1
    
    return render_template("quiz.html", message=message,quest=session["questions"][session["current_question"]]["Quest"], options=session["questions"][session["current_question"]]["Option"], final=final, current_number=session["current_question"] + 1, total_questions=len(session["questions"]))

@app.route("/result")
def result():
    score = session.get("score")
    number = len(session["questions"])
    percent = round((score / number) * 100, 2)
    remark = ""
    if 90 <= percent <= 100:
        remark = "Excellent! 🌟"
    elif 70 <= percent < 90:
        remark = "Good job! 👍"
    elif 50 <= percent < 70:
        remark = "Keep practicing 💪"
    else:
        remark = "Study more 📚"
    
    return render_template("result.html", score=score, number=number, percent=percent, remark=remark)
    
@app.route("/restart", methods=['POST'])
def restart():
    session.pop("answers", None)
    session.pop("score", None)
    session.pop("current_question", None)

    return redirect(url_for("quest"))








if __name__ == '__main__':
    app.run(debug=True)