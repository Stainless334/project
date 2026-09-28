from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    #message = ""
    
        #message = f"Recieved action: {action}"
    
    return render_template("index.html")

@app.route("/quiz", methods=['GET'])
def quest():
    message = ""
    if request.method == 'POST':
        action = request.form.get('button')
        message = f"{action}  Quiz page"
    return render_template("quiz.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)