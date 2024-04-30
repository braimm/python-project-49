import random

TASK_GAME = 'What number is missing in the progression?'


def play():
    start_progression = random.randint(1, 10)
    length_progression = random.randint(5, 10)
    step_progression = random.randint(1, 5)
    position_invisible_number = random.randint(0, length_progression - 1)
    progression = []
    for i in range(length_progression):
        progression.append(start_progression)
        start_progression += step_progression
    missing_number = progression[position_invisible_number]
    progression[position_invisible_number] = '..'
    missing_sequence = ' '.join(map(str, progression))
    return missing_sequence, missing_number
