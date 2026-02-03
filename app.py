from flask import Flask, render_template, redirect, url_for, flash, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/projects", methods=["GET"])
def projects():
    return render_template("project.html")


@app.route("/sketchbook", methods=["GET"])
def sketchbook():
    return render_template("sketchbook.html")


@app.route("/links", methods=["GET"])
def links():
    return render_template("links.html")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
