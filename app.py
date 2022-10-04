from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://giphy.com/gifs/funny-cat-12HZukMBlutpoQ",
    "https://giphy.com/gifs/tiger-cat-black-and-white-Cr7AfrUbRatmo",
    "https://giphy.com/gifs/bbcamerica-bbc-america-dynasties-553vlRAc1XZTVlAk3L",
    "https://giphy.com/gifs/bbcamerica-nature-elephant-bbc-america-ZCNhFJnP23twCGOzDg",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
