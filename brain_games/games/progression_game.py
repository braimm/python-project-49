import random
import prompt


def play(value):
    print('What number is missing in the progression?')
    for i in range(value):
        start_progression = random.randint(1, 10)
        length_progression = random.randint(5, 10)
        step_progression = random.randint(1, 5)
        position_invisible = random.randint(0, length_progression - 1)
        progression = [start_progression]
        for i in range(length_progression):
            start_progression += step_progression
            progression.append(start_progression)
        invisible = progression[position_invisible]
        progression[position_invisible] = '..'
        string_list = ' '.join(map(str, progression))
        print(f'Question: {string_list}')
        answer = prompt.integer('Your answer: ')
        if answer == invisible:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{invisible}'.")
            return False
    return True
