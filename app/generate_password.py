import random
import string
from app.exceptions import (
    PasswordTooLongException, 
    PasswordTooShortException, 
    InvalidCharsetException,
    EmptyCharsetException
)

def generate_password(charset_chosen=["uppercase", "lowercase", "digit", "special"], pass_length=8):

    if pass_length < 8:
        raise PasswordTooShortException
        
    if pass_length > 32:
        raise PasswordTooLongException

    password_string_dict = {
        "uppercase" : string.ascii_uppercase,
        "lowercase" : string.ascii_lowercase,
        "digit" : string.digits,
        "special" : string.punctuation
    }
    
    password = []
    charsets = []

    if charset_chosen == []:
        raise EmptyCharsetException

    charset_template = ["uppercase", "lowercase", "digit", "special"]
    for charset in charset_chosen:
        if charset not in charset_template:
            raise InvalidCharsetException
    
    for charset in charset_chosen:
        charsets.append(password_string_dict[charset])

    for charset in charsets:
        password += random.choice(charset)
        
    for i in range(pass_length - len(charset_chosen)):
        password += random.choice(''.join(charsets))

    random.shuffle(password)
    password_string = ''.join(password)
    
    return password_string