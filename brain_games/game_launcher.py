import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def game_success(name):
    print(f"Congratulations, {name}!")


def game_failed(name):
    print(f"Let's try again, {name}!")


def launch(version_game):
    name_user = welcome_user()
    AMOUNT_ROUND = 3
    if version_game.play(AMOUNT_ROUND):
        game_success(name_user)
    else:
        game_failed(name_user)
