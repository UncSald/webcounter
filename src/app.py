from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    if cnt.value != 0:
        cnt.reset()
    return redirect("/")

@app.route("/setvalue", methods=["POST"])
def set_value():
    cnt.set_value(request.form['value'])
    return redirect("/")