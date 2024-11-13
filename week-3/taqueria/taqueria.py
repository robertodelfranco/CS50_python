
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_value = 0.00;
    while True:
        try:
            key = input("Item: ").title();
            if key in menu:
                x = get_item(menu, key);
                total_value = total_value + x;
                print(f"Total: ${total_value:.2f}");
        except EOFError:
            print();
            break


def get_item(menu, key):
    return menu[key];


main()
