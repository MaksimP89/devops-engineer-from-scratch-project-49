from random import randint

from brain_games.logic.const import (
    QUESTION_1,
)
from brain_games.logic.utils import main_loop, welcome_user


def inp_func():
    tmp = randint(0, 100)
    expect = "yes" if tmp % 2 == 0 else "no"
    return expect, tmp


def main():
    USER_NAME = welcome_user()
    main_loop(
        input_func=inp_func, 
        question=QUESTION_1,
        user_name=USER_NAME,
                
      )
        
