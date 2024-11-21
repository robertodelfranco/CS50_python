import inflect

def main():
    listOfNames = []
    engine = inflect.engine()
    try:
        while True:
            name = input("Name: ")
            listOfNames.append(name)
    except EOFError:
        new_list = engine.join(listOfNames)
        print()
        print(f"Adieu, adieu, to {new_list}")

main()
