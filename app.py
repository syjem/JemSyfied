import re

from flask import Flask, render_template, flash, request, session, url_for, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Set Flask app environment to development
app.debug = 'development'

# Enable debug mode
app.debug = True

current_date = datetime.now().date()

@app.context_processor
def inject_current_year():
    current_year = datetime.now().year
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

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

SERVICES = [
    "Weddings",
    "Portraits",
    "Families",
    "Graduations",
    "Birthdays",
    "Other Occasions"
]

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        service = request.form.get("select_services")

        # Initialize an empty list to store validation errors
        errors = []

        # form validation
        if not name:
             errors.append("Please enter a valid name!")
        elif len(name) < 3:
            errors.append("Name is too short!")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Please enter a valid email!")
        if not date:
           errors.append("Please select a valid date!")
        elif datetime.strptime(date, '%Y-%m-%d').date() < current_date:
            errors.append("Please select dates that are not prior to the current date.")
        if service not in SERVICES:
            errors.append("Please select a valid service!")

        if errors:
            # If there are any errors, flash them all at once as error messages
            for error in errors:
                flash(error, category='error')

            # Render the form template with error messages and retained form data
            return render_template("contact.html", services=SERVICES, 
                                    name=name, email=email, date=date,
                                    selected_service=service
                                )

        else:
            flash("You have booked successfully!", category='success')
    
    return render_template("contact.html", services=SERVICES)





if __name__ == '__main__':
    app.run()