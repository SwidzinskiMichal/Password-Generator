from flask import Flask
from password_generator import password_generator
app = Flask(__name__)


@app.route('/')
def generate_password():
    password = password_generator()
    return "Your password is: " + password