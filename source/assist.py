import random


def chosen_number():
    random_number = random.randint(1, 5)
    return random_number


def count_point(guess_number):
    result = guess_number * 10
    if result == 30:
        return str(result) + " 🎉"
    elif result == 20:
        return str(result) + " 😎"
    elif result == 10:
        return str(result) + " 🙂"
    else:
        return str(result) + " 🤦‍♂️"
