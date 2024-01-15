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

#def true_answer():
#    print('Correct!')

def launch(version_game):
    name_user = welcome_user()
    amount_round = 3
    # запускается игра
    if version_game.play(amount_round):    
        game_success(name_user)
    else:
        game_failed(name_user)
 