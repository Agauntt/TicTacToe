# presentation/console/cli.py

import sys 

from library.src.game.engine import TicTacToe
from .args import parse_args
from .renderers import ConsoleRenderer


def main() -> None:
    player1, player2, starting_mark = parse_args()

    TicTacToe(player1, player2, ConsoleRenderer()).play(starting_mark)