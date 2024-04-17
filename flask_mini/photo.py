from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def flask():
    return render_template("photo1.html")

@app.route("/photo")
def greet():
    return render_template("photo2.html", name=request.args.get("name", "world"))
