import random
import prompt

def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    operaton_set = ['+', '-', '*']
    for i in range(3):
        operation = random.choice(operaton_set)
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        match operation:
            case '+':
                result_operation = number_1 + number_2
            case '-':
                result_operation = number_1 - number_2
            case '*':
                result_operation = number_1 * number_2
        print(f'Question: {number_1} {operation} {number_2}')
        answer = prompt.integer('Your answer: ')
        if result_operation == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result_operation}'.")
            return
    print(f"Congratulations, {name}!")
