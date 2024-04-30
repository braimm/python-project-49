import random


TASK_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    number = random.randint(1, 100)
    mod = (number % 2)
    if mod:
        even = 'no'
    else:
        even = 'yes'
    return number, even
