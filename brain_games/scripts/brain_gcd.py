import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.const import (
    ANSWER_OUT,
    CONGL,
    EXIT_2,
    GAME,
    INPUT_FROM_USER,
    QUESTION_3,
)
from brain_games.utils import (
    exit_from_game,
    get_input_from_user,
    get_int_from_user,
    main_execution,
)


def question():
    one = randint(0, 100)
    two = randint(0, 100)
    expr = f"{str(one)} {str(two)}"
    result = math.gcd(one, two)
    return expr, result


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_3)
    while run_game <= GAME:
        expr, expect = question()        
        imput_value = get_input_from_user(INPUT_FROM_USER.format(expr))
        imput_value = get_int_from_user(imput_value)
        run_game +=main_execution(
                answer_out=ANSWER_OUT.format(imput_value),
                inp_user=imput_value,
                expect=expect,
                exite_string=EXIT_2,
                format_ex_str=[
                    imput_value,
                    expect,
                    USER_NAME
                ]
            )

    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
