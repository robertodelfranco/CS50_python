import sys
from csv import reader
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        with open(sys.argv[1], 'r') as file:
            content = reader(file)
            table = list(content)
            headers = table.pop(0)
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()
