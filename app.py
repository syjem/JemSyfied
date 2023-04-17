import os
import datetime

from flask import Flask, render_template, flash, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash 

app = Flask(__name__)

# Set Flask app environment to development
app.debug = 'development'

# Enable debug mode
app.debug = True

@app.route("/")
def home():
    return render_template("index.html", current_year=datetime.datetime.now().year)

@app.route("/about")
def about():
    return render_template("about.html", current_year=datetime.datetime.now().year)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", current_year=datetime.datetime.now().year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=datetime.datetime.now().year)


if __name__ == '__main__':
    app.run()