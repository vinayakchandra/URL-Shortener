import string
import random
from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

# shortened_urls = {}
with open("urls.json", "r") as f:
    shortened_urls = json.load(f)


def generate_short_url(length=5):
    chars = string.ascii_letters + string.digits  # alphabets + digits
    short_url = "".join(random.choice(chars) for _ in range(length))  # random string of 'n' characters
    return short_url


@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']

        # if link already exists
        for key, value in shortened_urls.items():
            if long_url == value:
                short_url = key
                return f"Shortened URL : {request.url_root}{short_url}"

        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()

        shortened_urls[short_url] = long_url  # key : value
        with open("urls.json", "w") as f:
            json.dump(shortened_urls, f)
        return f"Shortened URL : {request.url_root}{short_url}"

    return render_template("index.html")


@app.route("/<short_url>", methods=["GET"])
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)  # get value of key
    if long_url:
        return redirect(long_url)  # redirect
    else:
        return "URL not found", 404


if __name__ == "__main__":
    app.run(debug=True)
