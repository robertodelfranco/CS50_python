import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        count = 0
        with open(sys.argv[1], 'r') as file:
            for line in file:
                if line.lstrip().startswith("#") or not line.strip():
                    continue
                count += 1
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()
