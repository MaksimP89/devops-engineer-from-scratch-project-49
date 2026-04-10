from random import randint

from brain_games.const import (
    EXIT_2,
    QUESTION_4,
)
from brain_games.utils import (
    main_loop,
    welcome_user,
)


def input_func():
    length = 10
    start = randint(1, 11)
    step = randint(1, 5)
    progression = [start + i * step for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]    
    progression[hidden_index] = '..'
    expr = ' '.join(str(x) for x in progression)
    return str(correct_answer), expr


def main():
    USER_NAME = welcome_user()
    main_loop(
        input_func=input_func,
        question=QUESTION_4,
        user_name=USER_NAME,
        exit=EXIT_2,
        exit_var=2,
        )


if __name__ == "__main__":
    main()
