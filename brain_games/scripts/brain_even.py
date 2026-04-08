from random import randint

from brain_games.cli import welcome_user
from brain_games.const import (
    ANSWER_OUT,
    CONGL,
    CORRECT,
    EXIT_1,
    GAME,
    INPUT_FROM_USER,
    QUESTION_1,
)
from brain_games.utils import exit_from_game, get_input_from_user


def is_even(num: int, ans: str) -> str:
    correct_ans = "yes" if num % 2 == 0 else "no"
    return True if correct_ans == ans else False


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_1)
    while run_game <= GAME:
        number = randint(0, 100)    
        answer = get_input_from_user(INPUT_FROM_USER.format(number))
        print(ANSWER_OUT.format(answer))
        if is_even(number, answer):
            print(CORRECT)
            run_game += 1
        else:
            exit_from_game(EXIT_1.format(USER_NAME))

    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
