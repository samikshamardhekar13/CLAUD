
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My Cloud Computing Practical</h1>
    <p>Hello from Google Colab!</p>
    <p>This program is ready for cloud deployment.</p>
    """

if __name__ == "__main__":
    app.run()
