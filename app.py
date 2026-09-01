from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/zaehler", methods=["GET", "POST"])
def zaehler():
    text, zeichen, woerter = "", 0, 0
    if request.method == "POST":
        text = request.form.get("text", "")
        zeichen = len(text)
        woerter = len(text.split())
    return render_template("zaehler.html", text=text, zeichen=zeichen, woerter=woerter)


if __name__ == "__main__":
    app.run(debug=True)
