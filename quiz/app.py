from flask import Flask, render_template, request, session, redirect, url_for
import quiz 

app = Flask(__name__)
app.secret_key = "the secret flash"

@app.route("/", methods=['GET'])
def home():
    #message = ""
    
        #message = f"Recieved action: {action}"
    
    return render_template("index.html")

@app.route("/quiz", methods=['GET', 'POST'])
def quest():
    message = ""
    if session.get("current_question") is None:
        session["current_question"] = 0
    if session.get("answers") is None:
        session["answers"] = {}
    final = session["current_question"] == (len(quiz.question) - 1)
    if request.method == 'POST':
        select = request.form.get('action')
        if select == 'previous':
            if session["current_question"] > 0:        
                session["current_question"] -= 1
        elif select == 'next':

            action = request.form.get('option')
            session["answers"][str(session["current_question"])] = action
            if session["current_question"] != (len(quiz.question) - 1):
                session["current_question"] += 1
        elif select == 'submit':
            action = request.form.get('option')
            session["answers"][str(session["current_question"])] = action
            score = 0
            for goal in session["answers"]:
                if session["answers"][goal] == quiz.question[int(goal)]["Ans"]:
                    score += 1
            session["score"] = score
            return redirect(url_for("result"))
    
    return render_template("quiz.html", message=message,quest=quiz.question[session["current_question"]]["Quest"], options=quiz.question[session["current_question"]]["Option"], final=final )
    
@app.route("/result")
def result():
    score = session.get("score")
    number = len(quiz.question)
    percent = round((score / number) * 100, 2)
    remark = ""
    if 100 >= percent <= 90:
        remark = "Excellent! 🌟"
    elif 90 > percent <= 70:
        remark = "Good job! 👍"
    elif 70 > percent <= 50:
        remark = "Keep practicing 💪"
    elif percent > 50:
        remark = "Study more 📚"
    """90–100% → Excellent! 🌟
70–89% → Good job! 👍
50–69% → Keep practicing 💪
Below 50% → Study more 📚"""
    return render_template("result.html", score=score, number=number, percent=percent, remark=remark)
    
@app.route("/restart", methods=['POST'])
def restart():
    session.pop("answers", None)
    session.pop("score", None)
    session.pop("current_question", None)

    return redirect(url_for("quest"))








if __name__ == '__main__':
    app.run(debug=True)