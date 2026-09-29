from flask import Flask, render_template, request
#from quiz import question

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
        if action == "Paris":
            message = "Correct!!"
        else:
            message = f"Wrong!"
    return render_template("quiz.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)