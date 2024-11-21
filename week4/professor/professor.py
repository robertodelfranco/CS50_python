import random
import sys


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "));
            if 1 <= level <= 3:
                return level;
        except ValueError:
            pass


def generate_integer(level):
    points = 0;
    if level == 1:
        i = 0;
        while i in range(10):
            x = random.randint(0, 9);
            y = random.randint(0, 9);
            points += catch_answer(x, y)
            i += 1;
    elif level == 2:
        i = 0;
        while i in range(10):
            x = random.randint(10, 99);
            y = random.randint(10, 99);
            points += catch_answer(x, y)
            i += 1;
    else:
        i = 0;
        while i in range(10):
            x = random.randint(100, 999);
            y = random.randint(100, 999);
            points += catch_answer(x, y)
            i += 1;
    print(f"Score: {points}")
    sys.exit()


def catch_answer(x, y):
    c = 0;
    while c < 3:
        try:
            print(f"{x} + {y} = ", end="")
            result = int(input(""));
            if result == (x + y):
                return 1;
            else:
                print("EEE")
                c += 1;
        except ValueError:
            print("EEE")
            c += 1;
            pass ;
    else:
        print(f"{x} + {y} = {x + y}")
        return 0


if __name__ == "__main__":
    main()
