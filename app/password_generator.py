import random
import string
from app.exceptions import PasswordTooLongException, PasswordTooShortException

def password_generator(pass_length = 8):

    if pass_length < 8:
        raise PasswordTooShortException
        
    if pass_length > 32:
        raise PasswordTooLongException


    password = []
    charsets = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]

    for charset in charsets:
        password += random.choice(charset)


    for i in range(pass_length - 4):
        password += random.choice("".join(charsets))

    random.shuffle(password)
    password_string = ''.join(password)

    return password_string