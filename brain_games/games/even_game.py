import random
import prompt
from brain_games import cli



def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    # name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
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
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
