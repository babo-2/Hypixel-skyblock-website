from flask import Flask, render_template, request
import os
import time

app = Flask(__name__)


@app.route('/')
def index():
    print("ip: " + request.remote_addr)
    return render_template("index.html", test="printme")


@app.route("/money-making-methods/")
def money_making_methods_index():
    return render_template("money-making-methods/index.html")


@app.route("/money-making-methods/<method>")
def money_making_methods(method=None):
    if method == None or method == "":
        return render_template("money-making-methods.html")

    langs = request.args
    lang = ""

    if "lang" in langs:
        lang = langs["lang"]
    lang = str(lang)
    time.sleep(0.1)
    return render_template("money-making-methods/" + method + ".html", lang=lang)


@app.route("/Skills/<method>")
def Skills(method=None):
    if method == None or method == "":
        return render_template("Skills/index.html")

    return render_template("money-making-methods/" + method)


@app.route("/Skills/")
def Skills_index():
    return render_template("Skills/index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT")
            if os.getenv("PORT") != None else "5000", debug=True)
