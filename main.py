from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
@app.route("/name")
def name():
    return "my name is Alvin this enterprice web development i build a flask !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))