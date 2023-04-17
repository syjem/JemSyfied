import os
import datetime

from flask import Flask, render_template, flash, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash 

app = Flask(__name__)

# Set Flask app environment to development
app.debug = 'development'

# Enable debug mode
app.debug = True

@app.context_processor
def inject_current_year():
    current_year = datetime.datetime.now().year
    return dict(current_year=current_year)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()