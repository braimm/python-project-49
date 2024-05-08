import random


TASK_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return False if num % 2 else True


def play():
    number = random.randint(1, 100)
    even_answer = "yes" if is_even(number) else 'no'
    return number, even_answer
