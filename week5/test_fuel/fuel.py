def main():
    fraction = input("Fraction: ");
    total_fuel = convert(fraction);
    print(gauge(total_fuel))


def convert(fraction):
    while True:
        try:
            one, two = fraction.split("/");
            number = int(one)
            division = int(two)
            result = number / division
            if result <= 1:
                return int(result * 100)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F";
    elif percentage <= 1:
        return "E";
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
