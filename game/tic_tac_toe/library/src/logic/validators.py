import re

from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.logic.models import Grid, GameState

from src.logic.exceptions import InvalidGameState


def validate_grid(grid:Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")
    

def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )


def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count > 1):
        raise InvalidGameState("Wrong number of Xs and Os")
    

def validate_starting_mark(grid:Grid, s_mark):
    pass


def validate_winner(grid:Grid, s_mark:str, winner:bool):
    pass