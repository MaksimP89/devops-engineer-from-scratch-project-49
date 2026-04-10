import math
from random import randint

from brain_games.logic.const import EXIT_2, QUESTION_3
from brain_games.logic.utils import main_loop, welcome_user


def input_func():
    one = randint(0, 100)
    two = randint(0, 100)
    expr = f"{str(one)} {str(two)}"
    result = math.gcd(one, two)    
    return str(result), expr


def main():
    USER_NAME = welcome_user()
    main_loop(
        input_func=input_func,
        question=QUESTION_3,
        user_name=USER_NAME,
        exit=EXIT_2,
        exit_var=2,
        )


