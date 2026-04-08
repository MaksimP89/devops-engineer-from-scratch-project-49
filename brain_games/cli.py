import prompt

from brain_games.const import HELLO


def welcome_user():
    print(HELLO)
    name = prompt.string("May I have your name?")
    print(f"Hellow, {name}")
