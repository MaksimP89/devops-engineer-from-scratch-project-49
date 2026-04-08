import prompt
import sys

from brain_games.const import CORRECT, EXCEPT_CHISLO


def get_input_from_user(str_out: str):
    input_str = prompt.string(str_out+' ')
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


def main_execution(answer_out:str,inp_user: str, expect: str,
                    exite_string:str,format_ex_str:list)->int:
    print(answer_out)
    if not inp_user == expect:
        exit_from_game(exite_string.format(*format_ex_str))
    print(CORRECT)    
    return 1








