from flask import Flask, render_template, redirect, url_for, flash, request
import os

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))