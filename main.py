"""
Solving 2048 using A*

Possible heuristics:
- Points
- Tiles removed
- New biggest tile

"""

from a_star_2048.board import (
    init_board,
    is_finished,
    move_board,
    print_board,
    spawn_value,
)

if __name__ == "__main__":
    current_play: list[list[int]] = init_board()

    last_play: list[list[int]] = []
    while True:
        if is_finished(current_play):
            print("You lost the game")
            break
        if current_play != last_play:
            last_play = current_play
            spawn_value(current_play)

        print_board(current_play)
        move = input("Choose move:\n")
        current_play = move_board(
            current_play,
            move,  # pyright: ignore[reportArgumentType]
        )
