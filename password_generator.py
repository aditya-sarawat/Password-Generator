import string
import random


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def get_password_length():
    length_of_password = input("How long do you want your password: ")
    return int(length_of_password)


def password_generator(cbl, password_length=8):
    # create alphanumerical by fetching string constant
    printable = fetch_string_constant(cbl)

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password
    random_password = random.choices(printable, k=password_length)

    # convert generated password to string
    random_password = ''.join(random_password)
    return random_password


def password_combination_choice():
    # retrieve a user's password character combination choice
    want_digits = input("Want digits ? (True or False) : ")
    want_letters = input("Want letters ? (True or False): ")
    want_punts = input("Want punctuation ? (True or False): ")

    # convert those choices from string to it's right boolean type
    try:
        want_digits = eval(want_digits.title())
        want_punts = eval(want_punts.title())
        want_letters = eval(want_letters.title())
        return [want_digits, want_letters, want_punts]

    except NameError as e:
        print("\nInvalid value. Use either True or False")
        print("Try to regenerate.\n")

    return [True, True, True]


def fetch_string_constant(choices):
    string_constant = ''

    string_constant += NUMBERS if choices[0] else ''
    string_constant += LETTERS if choices[1] else ''
    string_constant += PUNCTUATION if choices[2] else ''

    return string_constant


if __name__ == '__main__':
    print("""
        Welcome To the Password Generator Program
               Made By : Aditya Sarawat
               
               
        """)

    length = get_password_length()
    choice_list = password_combination_choice()
    password = password_generator(choice_list, length)

    print('Your Password is Generated: ' + password)
    print('\nThanks for using password generator program.')
