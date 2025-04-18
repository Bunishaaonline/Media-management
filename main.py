from flask import Flask
from content_generator import generate_daily_post

app = Flask(__name__)

@app.route("/")
def home():
    return "ShopBooksBot is live!"

@app.route("/daily-post")
def daily_post():
    return generate_daily_post()

if __name__ == "__main__":
    app.run(debug=True)
