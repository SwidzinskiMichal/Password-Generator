from flask import escape, render_template, request
from app import app
from app.generate_password import generate_password


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        charset_chosen = request.form.getlist("charsets")
        password = generate_password(charset_chosen=charset_chosen)
        return render_template("view_password.html", password=password)
       # return escape("Your password is: " + password)
    return render_template("index.html")