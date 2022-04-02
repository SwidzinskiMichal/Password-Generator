from flask import escape

from app import app
from app.password_generator import password_generator

@app.route('/')
def generate_password():
    password = password_generator()
    print(password)
    return escape("Your password is: " + password)
