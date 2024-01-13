import random
import prompt


def play(value):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(value):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        mod = (number % 2)
        if ((mod == 0) and (answer == 'yes')) or ((mod != 0) and (answer == 'no')):
            print('Correct!')
        else:
            if mod == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return False
    return True
