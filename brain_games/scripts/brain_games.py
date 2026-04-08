import prompt

from brain_games.const import HELLO


def main():
    print(HELLO)
    name = prompt.string("May I have your name?")
    print(f"Hellow, {name}")


if __name__ == "__main__":
    main()
