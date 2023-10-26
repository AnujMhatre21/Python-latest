import random
import string
# MINI python prject by TEch wth tim


def generate_password(min_length, numbers=True, special_charaters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.special_charaters

    charaters = letters
    if numbers:
        charaters += digits
    if special_characcters:
        charaters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        if new_char in special:
            has_special = True


generate_password(10)
