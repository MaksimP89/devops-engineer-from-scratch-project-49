# import prompt

from brain_games.const import HELLO, PROGRAM_NACHALO
from brain_games.utils import get_input_from_user


def welcome_user():
    print(HELLO)
    # USER_NAME = prompt.string("May I have your name?")
    # USER_NAME = USER_NAME.strip().capitalize()
    USER_NAME = get_input_from_user(PROGRAM_NACHALO)
    USER_NAME = USER_NAME.capitalize()
    print(f"Hellow, {USER_NAME}")
    return USER_NAME
