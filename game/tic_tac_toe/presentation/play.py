# presentation/play.py
import os, sys

from library.src.game.engine import TicTacToe
from library.src.game.players import RandomComputerPlayer
from library.src.logic.models import Mark
from console.renderers import ConsoleRenderer
from console.players import ConsolePlayer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()