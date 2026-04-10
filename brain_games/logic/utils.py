import sys

import prompt

from brain_games.logic.const import (
    ANSWER_OUT,
    CONGL,
    CORRECT,
    GAME,
    HELLO,
    INPUT_FROM_USER,
    PROGRAM_NACHALO,
)


def welcome_user():
    print(HELLO)
    USER_NAME = get_input_from_user(PROGRAM_NACHALO, 1)
    USER_NAME = USER_NAME.capitalize()
    print(f"Hello, {USER_NAME}")
    return USER_NAME


def main_loop(input_func: callable, question: str, user_name: str,
              exit: str, exit_var: int):
    run_game = 0
    print(question)
    while run_game < GAME:
        expect, result = input_func()
        input_value = get_input_from_user(INPUT_FROM_USER.format(result), 2)
        print(ANSWER_OUT.format(input_value))
        add_exit_string = []
        add_exit_string.append(user_name)
        if exit_var != 1:
            add_exit_string.insert(0, expect)
            add_exit_string.insert(0, input_value)
            
        run_game += main_execution(
            inp_user=input_value,
            expect=expect,
            exite_string=exit,
            format_param=add_exit_string,
        )
    print(CONGL.format(user_name))


def main_execution(inp_user: str, expect,
                   exite_string: str, format_param: list) -> int:
    
    if not inp_user == expect:
        exit_from_game(exite_string, format_param)
        
    print(CORRECT)    
    
    return 1


def get_input_from_user(str_out: str,type_emtry:int):
    if type_emtry == 1 :
        input_str = prompt.string(str_out, True)
    else:
        input_str = prompt.secret(str_out)
    return input_str


def exit_from_game(exit_string: str, param) -> None:
    print(exit_string.format(*param))
    sys.exit()









