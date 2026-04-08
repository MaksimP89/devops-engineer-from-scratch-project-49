import sys
from random import randint, choice

import prompt

from brain_games.cli import welcome_user
from brain_games.const import GAME, RESULT, CONGL, WRONG_ANSW, QUESTION, EXCEPT_CHISLO


def question() -> (str, int):
    one = randint(0, 100)
    two = randint(0, 100)
    lst = ["+", "-", "*"]
    expr = f"{str(one)} {choice(lst)} {str(two)}"
    result = eval(expr)
    return expr, result


def chec_result(input, r_answ) -> bool:
    return True if r_answ == input else False


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(RESULT)
    while run_game <= GAME:
        expr, r_result = question()
        inp = prompt.string(QUESTION.format(expr))
        try:
            inp = int(inp)
            if chec_result(inp, r_result):
                run_game += 1
            else:
                print(WRONG_ANSW.format(str(inp), str(r_result)))
                sys.exit()
        except ValueError:
            print(EXCEPT_CHISLO)
            sys.exit()

    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
