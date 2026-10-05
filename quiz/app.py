from flask import Flask, render_template, request, session
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
       
    
    return render_template("quiz.html", message=message,quest=quiz.question[session["current_question"]]["Quest"], options=quiz.question[session["current_question"]]["Option"], final=final )

@app.route("/result")
def result():
    return render_template("result.html")
    










if __name__ == '__main__':
    app.run(debug=True)