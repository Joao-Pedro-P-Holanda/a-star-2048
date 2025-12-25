"""
Solving 2048 using A*

Possible heuristics:
- Points
- Tiles removed
- Possible removals
- New biggest tile

"""

from .board import (
    init_board,
    move_board,
    print_board,
    spawn_value,
)

if __name__ == "__main__":
    current_play: list[list[int]] = init_board()

    last_play: list[list[int]] = []
    while True:
        if current_play != last_play:
            last_play = current_play
            spawn_value(current_play)

        print_board(current_play)
        move = input("Choose move:\n")
        current_play = move_board(
            current_play,
            move,  # pyright: ignore[reportArgumentType]
        )
