# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    password=''
    pointer=0

    for i in range(random.randint(8, 16)):
        if(pointer == 0):
            password += random.choice(string.ascii_lowercase)
            pointer = 1
        elif(pointer == 1):
            password += random.choice(string.ascii_uppercase)
            pointer = 2
        elif(pointer== 2):
            password += random.choice(string.digits)
            pointer = 3
        else:
            password += SYMBOLS[random.randint(0, len(SYMBOLS)-1)]
            pointer = 0

    password = ''.join(random.sample(password, len(password)))
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
