import sys
from csv import DictWriter, DictReader

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        with open(sys.argv[1], 'r', newline='') as file:
            content = DictReader(file)
            fieldnames = ['first', 'last', 'house']
            with open(sys.argv[2], 'w', newline='') as f:
                writer = DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for row in content:
                    names = row['name'].split(',')
                    writer.writerow({'first': names[1].lstrip(), 'last': names[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == '__main__':
    main()
