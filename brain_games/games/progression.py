import random

TASK_GAME = 'What number is missing in the progression?'


def get_progression(start, length, step):
    progression = []
    for i in range(length):
        progression.append(start)
        start += step
    return progression


def play():
    start = random.randint(1, 10)
    length = random.randint(5, 10)
    step = random.randint(1, 5)
    progression = get_progression(start, length, step)
    position_invisible_number = random.randint(0, length - 1)
    missing_number = progression[position_invisible_number]
    progression[position_invisible_number] = '..'
    missing_sequence = ' '.join(map(str, progression))
    return missing_sequence, missing_number
