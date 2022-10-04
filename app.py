from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528",
    "https://tenor.com/view/lion-king-lion-animal-windy-gif-16642021",
    "https://tenor.com/view/tiger001-gif-24830104",
    "https://tenor.com/view/baby-elephant-trunk-dancing-gif-26449205",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
