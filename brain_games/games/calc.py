from random import choice, randint

from brain_games.logic.const import (
    EXIT_2,
    QUESTION_2,
)
from brain_games.logic.utils import (
    main_loop,
    welcome_user,
)


def input_func():
    one = randint(0, 100)
    two = randint(0, 100)
    lst = ['+', '-',]
    expr = f"{str(one)} {choice(lst)} {str(two)}"
    result = eval(expr)
    
    return str(result), expr


def main():
    USER_NAME = welcome_user()
    main_loop(
        input_func=input_func,
        question=QUESTION_2,
        user_name=USER_NAME,
        exit=EXIT_2,
        exit_var=2,
        )


