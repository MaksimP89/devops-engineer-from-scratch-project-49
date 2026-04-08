import sys
from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.const import ANSWER, EXIT, GAME


def is_even(num: int, ans: str) -> str:
    is_even = num % 2 == 0
    correct_ans = "yes" if is_even else "no"
    return True if correct_ans == ans else False


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(ANSWER)
    while run_game <= GAME:
        number = randint(0, 100)
        question = f"Question: {number}"
        print(question)
        answer = prompt.string("Your answer: ").strip().lower()
        if is_even(number, answer):
            run_game += 1
        else:
            sys.exit(EXIT.format(USER_NAME))

    print("Congratulations,", USER_NAME)


if __name__ == "__main__":
    main()
