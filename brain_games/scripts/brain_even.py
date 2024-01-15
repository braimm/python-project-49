#!/usr/bin/env python3

from brain_games.games import even_game
from brain_games import game_launcher


def main():
    game_launcher.launch(even_game)


if __name__ == '__main__':
    main()
