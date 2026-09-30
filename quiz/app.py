from flask import Flask, render_template, request, session
import quiz 

app = Flask(__name__)

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
        if action == quiz.question[0]["Ans"]:
            message = "Correct!!"
        else:
            message = "Wrong!"
    return render_template("quiz.html", message=message,quest=quiz.question[0]["Quest"], options=quiz.question[0]["Option"] )

if __name__ == '__main__':
    app.run(debug=True)