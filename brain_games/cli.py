import prompt

from brain_games.const import HELLO


def welcome_user():
    print(HELLO)
    USER_NAME = prompt.string("May I have your name?")
    USER_NAME = USER_NAME.strip().capitalize()
    print(f"Hellow, {USER_NAME}")
    return USER_NAME
