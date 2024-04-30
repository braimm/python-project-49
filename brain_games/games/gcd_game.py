import random

TASK_GAME = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    mod = num_1 % num_2
    if mod == 0:
        return num_2
    else:
        return get_gcd(num_2, mod)


def play():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    if number_1 >= number_2:
        result_gcd = get_gcd(number_1, number_2)
    else:
        result_gcd = get_gcd(number_2, number_1)
    pair_numbers = f'{number_1} {number_2}'
    return pair_numbers, result_gcd
