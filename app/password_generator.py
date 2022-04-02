import random
from app.exceptions import PasswordTooLongException, PasswordTooShortException

def password_generator(pass_length = 8):
    if pass_length < 8:
        raise PasswordTooShortException
        
    if pass_length > 32:
        raise PasswordTooLongException

    characters_range = range(33, 127)
    password = ''
    for i in range(pass_length):
        password += chr(random.choice(characters_range))
    
    return password