import random
import prompt

def check_prime(number):
    count_divider = 0
    for i in range(2, (number//2)+1):
        if (number % i) == 0:
            count_divider += 1
    if count_divider == 0:
        return True
    else:
        return False


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    # name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        status_number = check_prime(number)
        if ((answer == 'yes') and (status_number == True)) or ((answer == 'no') and (status_number == False)):
            print('Correct!')
        else:
            if status_number == True:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

prime_game()
