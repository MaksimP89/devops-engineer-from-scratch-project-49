import sys
from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.const import ANSWER, EXIT


def main():
    USER_NAME = welcome_user()

    run_game = 0
    print(ANSWER)
    while run_game <= 2:
        number = randint(0, 100)
        question = f"Question: {number}"
        print(question)
        answer = prompt.string("Your answer: ").strip().lower()
        is_even = number % 2 == 0
        correct_ans = "yes" if is_even else "no"

        if answer == correct_ans:
            run_game += 1
        else:
            print(EXIT.format(USER_NAME))
            sys.exit()

    print("Congratulations,", USER_NAME)


if __name__ == "__main__":
    main()
