from random import choice, randint

from brain_games.cli import welcome_user
from brain_games.const import (
    CONGL,
    CORRECT,
    EXIT_2,
    GAME,
    INPUT_FROM_USER,
    QUESTION_2,
)
from brain_games.utils import (
    exit_from_game,
    get_input_from_user,
    get_int_from_user,
)


def question():
    one = randint(0, 100)
    two = randint(0, 100)
    lst = ['+', '-','*']
    expr = f"{str(one)} {choice(lst)} {str(two)}"
    result = eval(expr)
    return expr, result


def chec_result(input, r_answ) -> bool:
    return True if r_answ == input else False


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_2)
    while run_game <= GAME:
        expr, r_result = question()
        imp = get_input_from_user(INPUT_FROM_USER.format(expr))
        imp = get_int_from_user(imp)
        if chec_result(imp, r_result):
            print(CORRECT)
            run_game += 1
        else:
            exit_from_game(EXIT_2.format(str(imp), str(r_result), USER_NAME))

    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
