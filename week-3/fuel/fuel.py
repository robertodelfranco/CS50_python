def main():
    while True:
        try:
            list = input("Fraction: ").split("/");
            x = int(list[0]);
            y = int(list[1]);
            if x <= y and y != 0:
                convert(x, y);
                break;
        except ValueError:
            pass;


def convert(x, y):
    total_fuel = (float(x) / float(y)) * 100;

    if total_fuel >= 99:
        print("F");
    elif total_fuel <= 1:
        print("E");
    else:
        print(f"{round(total_fuel)}%");


main()
