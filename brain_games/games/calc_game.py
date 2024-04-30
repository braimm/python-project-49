import random


TASK_GAME = 'What is the result of the expression?'


def play():
    OPERATION_SET = ['+', '-', '*']
    operation = random.choice(OPERATION_SET)
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    match operation:
        case '+':
            result_expression = number_1 + number_2
        case '-':
            result_expression = number_1 - number_2
        case '*':
            result_expression = number_1 * number_2
    expression = f'{number_1} {operation} {number_2}'
    return expression, result_expression
