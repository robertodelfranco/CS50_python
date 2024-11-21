import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            num = random.randint(1, level);
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess > 0:
                        if guess == num:
                            print("Just right!")
                            sys.exit() ;
                        elif guess > num:
                            print("Too large!")
                            continue ;
                        else:
                            print("Too small!")
                            continue ;
                except ValueError:
                    pass
        except ValueError:
            pass


main()
