from brain_games.cli import welcome_user
from brain_games.logic.utils import get_input_from_user


def main():
    USER_NAME = get_input_from_user()
    USER_NAME = USER_NAME.capitalize()
    print(f"Hellow, {USER_NAME}")


if __name__ == "__main__":
    main()
