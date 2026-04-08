import sys

import prompt

from brain_games.const import EXCEPT_CHISLO


def get_input_from_user(str_out: str):
    input_str = prompt.string(str_out)
    return input_str


def get_int_from_user(input: str) -> int:

    try:
        input = int(input)
    except ValueError:
        print(EXCEPT_CHISLO)

    return input


def exit_from_game(exit_string: str) -> None:
    print(exit_string)
    sys.exit()
