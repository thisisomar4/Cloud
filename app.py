from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif",
    "https://media.giphy.com/media/3otPoUGBfbuOgFhcpW/giphy.gif",
    "https://media.giphy.com/media/1Ygkk70ho1h6YrK6oC/giphy.gif",
    "https://media.giphy.com/media/l1TJVLJM0hfnGJjE4t/giphy.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
