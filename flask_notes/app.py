from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def flask():
    return render_template("flask.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))
