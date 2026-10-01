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

    if request.method == 'POST':
        action = request.form.get('option')
        if action == quiz.question[session["current_question"]]["Ans"]:
            message = "Correct!!"
        else:
            message = "Wrong!"
        if session["current_question"] != (len(quiz.question) - 1):
            session["current_question"] += 1
             
    if session.get("current_question") is None:
            session["current_question"] = 0


    return render_template("quiz.html", message=message,quest=quiz.question[session["current_question"]]["Quest"], options=quiz.question[session["current_question"]]["Option"] )

if __name__ == '__main__':
    app.run(debug=True)