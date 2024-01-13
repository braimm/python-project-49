import random
import prompt

def get_gcd(num_1, num_2):
    mod = num_1 % num_2
    if mod == 0:
        return num_2
    else:
        return get_gcd(num_2, mod)

def gcd_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    # name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        if number_1 >= number_2:
            result_gcd = get_gcd(number_1, number_2)
        else:
            result_gcd = get_gcd(number_2, number_1)
        print(f'Question: {number_1} {number_2}')
        answer = prompt.integer('Your answer: ')
        if answer == result_gcd:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result_gcd}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

# gcd_game()
