from flask import escape, render_template, request
from app import app
from app.password_generator import password_generator


@app.route('/', methods=['GET', 'POST'])
def checkboxes():
    if request.method == "POST":
        charset_chosen = request.form.getlist("mycheckbox")
        password = password_generator(charset_chosen=charset_chosen)
        return escape("Your password is: " + password)
    return render_template("checkboxes.html")
