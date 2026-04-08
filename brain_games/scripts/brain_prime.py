import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.const import (
    ANSWER_OUT,
    CONGL,
    EXIT_2,
    GAME,
    INPUT_FROM_USER,
    QUESTION_5,
)
from brain_games.utils import (
    get_input_from_user,
    main_execution,
    is_prime,
)


def question():
    number = randint(1, 100)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct    

def main():
    USER_NAME = welcome_user()
    run_game = 0
    print(QUESTION_5)    
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
