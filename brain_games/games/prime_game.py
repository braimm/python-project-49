import random

TASK_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    count_divider = 0
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, (number // 2) + 1):
        if (number % i) == 0:
            count_divider += 1
    if count_divider == 0:
        return True
    else:
        return False


def play():
    number = random.randint(1, 100)
    if check_prime(number):
        prime = 'yes'
    else:
        prime = 'no'
    return number, prime
