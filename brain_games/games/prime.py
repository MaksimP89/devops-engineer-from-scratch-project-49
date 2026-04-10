from random import randint

from brain_games.logic.const import (
    QUESTION_5,
)
from brain_games.logic.utils import (
    main_loop,
    welcome_user,
)


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


def input_func():
    number = randint(1, 100)
    correct = "yes" if is_prime(number) else "no"    
    return correct, str(number)     


def main():
    USER_NAME = welcome_user()
    
    main_loop(
        input_func=input_func,
        question=QUESTION_5,
        user_name=USER_NAME,
        )

