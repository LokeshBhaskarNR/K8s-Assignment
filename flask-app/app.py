from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    welcome = os.getenv("WELCOME_MSG", "Hello!")
    secret_key = os.getenv("SECRET_KEY", "Not Found")
    return f"""
    <h1>{welcome}</h1>
    <p><b>Secret Key:</b> {secret_key}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
