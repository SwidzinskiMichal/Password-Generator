import random
from app.exceptions import PasswordTooLongException, PasswordTooShortException

def password_generator(pass_length = 8):
    while True:
        result_isupper = False
        result_islower = False

        if pass_length < 8:
            raise PasswordTooShortException
            
        if pass_length > 32:
            raise PasswordTooLongException

        characters_range = range(33, 127)
        password = ''
        for i in range(pass_length):
            password += chr(random.choice(characters_range))    

        for character in password:
            if character.isupper():
                result_isupper = True

        for character in password:
            if character.islower():
                result_islower = True

        if result_isupper == True and result_islower == True:
            break
        else:
            pass             

    return password