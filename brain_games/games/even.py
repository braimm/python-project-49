from brain_games.games.generator import get_number


TASK_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return False if num % 2 else True


def play():
    number = get_number(1, 100)
    even_answer = "yes" if is_even(number) else 'no'
    return number, even_answer
