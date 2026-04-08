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
from brain_games.utils import exit_from_game, get_input_from_user, main_execution


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_1)
    while run_game <= GAME:
        number = randint(0, 100)    
        input_value = get_input_from_user(INPUT_FROM_USER.format(number))
        run_game +=main_execution(
            answer_out=ANSWER_OUT.format(input_value),
            inp_user=input_value,
            expect="yes" if number % 2 == 0 else "no",
            exite_string=EXIT_1,
            format_ex_str=[USER_NAME,],
        )

        
    print(CONGL.format(USER_NAME))


if __name__ == "__main__":
    main()
