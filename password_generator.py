import random


def password_generator(pass_length = 8):

    characters_range = range(33, 127)
    password = ''
    for i in range(pass_length):
        password += chr(random.choice(characters_range))
    
    return password

print(password_generator())