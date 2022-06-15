from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "i lvoe coding"

@app.route("/")
def start_page():
    return render_template("index.html")

@app.route("/survey/new", methods=['POST'])
def info():
    session["info"] = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    return redirect("/survey/result")

@app.route("/survey/result")
def results():
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)