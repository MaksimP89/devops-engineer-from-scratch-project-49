from random import randint
import sys

import prompt

from brain_games.const import ANSWER_OUT, CONGL, CORRECT, EXCEPT_CHISLO, GAME, INPUT_FROM_USER,PROGRAM_NACHALO,HELLO

def welcome_user():
    print(HELLO)
    USER_NAME = get_input_from_user(PROGRAM_NACHALO)
    USER_NAME = USER_NAME.capitalize()
    print(f"Hellow, {USER_NAME}")
    return USER_NAME


def main_loop(input_func,question,user_name,exit,*args):
    run_game = 0
    print(question)
    while run_game <= GAME:
        expect,result = input_func()
        input_value = get_input_from_user(INPUT_FROM_USER.format(result))
        run_game += main_execution(
            inp_user=input_value,
            expect=expect,
            exite_string=exit,
            format_ex_str=args,
        )
    print(CONGL.format(user_name))


def main_execution(inp_user: str,expect,
                   exite_string: str, format_ex_str: list) -> int:
    
    if not inp_user == expect:
        if not format_ex_str:
            exit_from_game(exite_string)
        else:
            exit_from_game(exite_string.format(*format_ex_str))    
    
    print(CORRECT)    
    
    return 1












def get_input_from_user(str_out: str):
    input_str = prompt.string(str_out + '\n', True)
    return input_str


def get_int_from_user(input: str) -> int:

    try:
        input = int(input)
    except ValueError:
        print(EXCEPT_CHISLO)

    return input


def exit_from_game(exit_string: str) -> None:
    print(exit_string)
    sys.exit()




def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True







