import random

TASK_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, (number // 2) + 1):
        if (number % i) == 0:
            return False
    return True


def play():
    number = random.randint(1, 100)
    prime = 'yes' if check_prime(number) else 'no'
    return number, prime
