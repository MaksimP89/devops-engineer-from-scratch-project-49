import sys


from brain_games.scripts.brain_calc import main as calc
from brain_games.scripts.brain_even import main as even
from brain_games.logic.const import EXCEPT_CHISLO, GAMES, GM
from brain_games.logic.utils import get_input_from_user
from brain_games.scripts.brain_gcd import main as gcd
from brain_games.scripts.brain_prime import main as prime
from brain_games.scripts.brain_progression import main as progressions

def main():
    inp =get_input_from_user(GAMES)
    try:
        inp=int(inp)
        match inp:
            case 1:
                even()
            case 2:
                calc()
            case 3:
                gcd()
            case 4:
                progressions()    
            case 5:
                prime()    
            case _:
                print(GM)
                sys.exit()
    except ValueError:
        print(EXCEPT_CHISLO)
        sys.exit()

if __name__ == "__main__":
    main()