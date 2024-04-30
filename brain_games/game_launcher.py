import prompt

AMOUNT_ROUND = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def game_success(name):
    print(f"Congratulations, {name}!")


def game_failed(name):
    print(f"Let's try again, {name}!")


def round_success():
    print('Correct!')


def round_failed(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")


def launch(name_game):
    name_user = welcome_user()
    print(name_game.TASK_GAME)
    round = 0
    while round < AMOUNT_ROUND:
        question, correct_answer = name_game.play()
        print(f"Question: {question}")
        if type(correct_answer) is int:
            user_answer = prompt.integer('Your answer: ')
        else:
            user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            round_success()
        else:
            round_failed(user_answer, correct_answer)
            game_failed(name_user)
            return
        round += 1
    game_success(name_user)
