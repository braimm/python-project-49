import random

TASK_GAME = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    if num_1 < num_2:
        buffer = num_1
        num_1 = num_2
        num_2 = buffer
    mod = num_1 % num_2
    return num_2 if mod == 0 else get_gcd(num_2, mod)


def play():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    pair_numbers = f'{number_1} {number_2}'
    result_gcd = get_gcd(number_1, number_2)
    return pair_numbers, result_gcd
