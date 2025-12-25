"""
Solving 2048 using A*

Possible heuristics:
- Points
- Tiles removed
- Possible removals
- New biggest tile

"""

from board import (
    set_empty_positions,
    move_board,
    print_board,
    spawn_value,
    SQUARE_SIZE,
)

if __name__ == "__main__":
    current_play: list[list[int]] = [[0] * SQUARE_SIZE for _ in range(SQUARE_SIZE)]

    last_play: list[list[int]] = []
    while True:
        if current_play != last_play:
            last_play = current_play
            set_empty_positions(current_play)
            spawn_value(current_play)

        print_board(current_play)
        move = input("Choose move:\n")
        current_play = move_board(
            current_play,
            move,  # pyright: ignore[reportArgumentType]
        )
