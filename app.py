import string
import secrets
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

@app.route("/temperatur", methods=["GET", "POST"])
def temperatur():
    celsius = fahrenheit = None
    if request.method == "POST":
        try:
            celsius = float(request.form.get("celsius", "").replace(",", "."))
            fahrenheit = round(celsius * 9 / 5 + 32, 1)
        except ValueError:
            celsius = None
    return render_template("temperatur.html", celsius=celsius, fahrenheit=fahrenheit)

@app.route("/passwort", methods=["GET", "POST"])
def passwort():
    pw, laenge = None, 16
    if request.method == "POST":
        laenge = max(4, min(64, int(request.form.get("laenge", 16))))
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        pw = "".join(secrets.choice(alphabet) for _ in range(laenge))
    return render_template("passwort.html", pw=pw, laenge=laenge)


if __name__ == "__main__":
    app.run(debug=True)
