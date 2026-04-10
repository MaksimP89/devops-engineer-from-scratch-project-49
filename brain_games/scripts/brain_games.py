from brain_games.logic.const import HELLO, PROGRAM_NACHALO
from brain_games.logic.utils import get_input_from_user, welcome_user


def main():
    print(HELLO)
    USER_NAME = get_input_from_user(PROGRAM_NACHALO)
    USER_NAME = USER_NAME.capitalize()
    print(f"Hellow, {USER_NAME}")
    return USER_NAME


if __name__ == "__main__":
    main()
