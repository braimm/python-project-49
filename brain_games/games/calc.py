import random


TASK_GAME = 'What is the result of the expression?'


def calculate(num_1, num_2, operator):
    match operator:
        case '+':
            result_expression = num_1 + num_2
        case '-':
            result_expression = num_1 - num_2
        case '*':
            result_expression = num_1 * num_2
    return result_expression


def play():
    OPERATIONS_SET = ['+', '-', '*']
    operation = random.choice(OPERATIONS_SET)
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    result_expression = calculate(number_1, number_2, operation)
    expression = f'{number_1} {operation} {number_2}'
    return expression, result_expression
