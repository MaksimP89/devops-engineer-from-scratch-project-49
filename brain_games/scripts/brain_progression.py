import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.const import (
    ANSWER_OUT,
    CONGL,
    CORRECT,
    EXIT_2,
    GAME,
    INPUT_FROM_USER,
    QUESTION_3,
)
from brain_games.utils import (
    exit_from_game,
    get_input_from_user,
    get_int_from_user,
)


def question():
    
    return expr, result


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_3)
    while run_game <= GAME:
        expr, result = question()        
        inp = get_input_from_user(INPUT_FROM_USER.format(expr))
        inp = get_int_from_user(inp)
        print(ANSWER_OUT.format(inp))

        if inp == result:
            print(CORRECT)
            run_game += 1
        else:
            exit_from_game(EXIT_2.format(inp, result, USER_NAME))

    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
