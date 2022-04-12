from flask import escape, render_template, request
from app import app
from app.generate_password import generate_password


@app.route('/', methods=['GET', 'POST'])
def checkboxes():
    if request.method == "POST":
        charset_chosen = request.form.getlist("mycheckbox")
        password = generate_password(charset_chosen=charset_chosen)
        return escape("Your password is: " + password)
    return render_template("checkboxes.html")
