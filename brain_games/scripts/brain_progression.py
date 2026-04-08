import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.const import (
    ANSWER_OUT,
    CONGL,
    EXIT_2,
    GAME,
    INPUT_FROM_USER,
    QUESTION_4,
)
from brain_games.utils import (
    exit_from_game,
    get_input_from_user,
    get_int_from_user,
    main_execution,
)


def question():
    length = 10
    start = randint(1, 11)
    step = randint(1, 5)
    progression = [start + i * step for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index] 
    progression[hidden_index] = '..'
    print(correct_answer)
    expr = ' '.join(str(x) for x in progression)
    return expr, str(correct_answer)


def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_4)    
    while run_game <= GAME:
        expr, r_result = question()
        imput_value = get_input_from_user(INPUT_FROM_USER.format(expr))       
        run_game += main_execution(
            answer_out=ANSWER_OUT.format(imput_value),
            inp_user=imput_value,
            expect=r_result,
            exite_string=EXIT_2,
            format_ex_str=[imput_value,r_result,USER_NAME],            
        )
        
    print(CONGL.format(USER_NAME))

    

if __name__ == "__main__":
    main()
