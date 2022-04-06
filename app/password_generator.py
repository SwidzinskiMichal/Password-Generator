import random
import string
from app.exceptions import PasswordTooLongException, PasswordTooShortException

def password_generator(pass_length = 8):

    if pass_length < 8:
        raise PasswordTooShortException
        
    if pass_length > 32:
        raise PasswordTooLongException


    characters_range = range(33, 127)
    password = []

    password += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits)

    for i in range(pass_length - 3):
        password += chr(random.choice(characters_range))    

    random.shuffle(password)
    password_string = ''.join(password)

    return password_string