#!/usr/bin/env python3

from brain_games.games import gcd_game
from brain_games import game_launcher


def main():
    game_launcher.launch(gcd_game)


if __name__ == '__main__':
    main()