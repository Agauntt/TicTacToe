# src/game/engine.py

from dataclasses import dataclass
from typing import Callable, TypeAlias

from library.src.game.players import Player
from library.src.game.renderers import Renderer
from library.src.logic.exceptions import InvalidMove
from library.src.logic.models import GameState, Grid, Mark
from library.src.logic.validators import validate_players

ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    renderer: Renderer
    error_handler: ErrorHandler | None = None


    def __post__init__(self):
        validate_players(self.player1, self.player2)


    def play(self, starting_mark:Mark=Mark("X")) -> None:
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as e:
                if self.error_handler:
                    self.error_handler(e)

    
    def get_current_player(self, game_state:GameState) -> Player:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2


