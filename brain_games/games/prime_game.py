import random
import prompt


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


def play(value):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(value):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        status_number = check_prime(number)
        if (((answer == 'yes') == status_number)
                or ((answer == 'no') != status_number)):
            print('Correct!')
        else:
            if status_number:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'yes'.")
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'no'.")
            return False
    return True
