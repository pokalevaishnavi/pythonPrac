from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 45,
        "Radha":99,
        "Mark":46,
        "Jeff":67,
        "Alexa":90,
        "Lily":100
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)