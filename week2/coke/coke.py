"""

Condition to print a variable num too:

print(f"This is a number {four}%");

"""

def main():
    change = 50;
    while change > 0:
        print("Amount Due: ", end="");
        print(change);
        coin = int(input("Insert Coin: "));
        change = subtract(change, coin);

    if change < 0:
        print("Change Owed: ", end="");
        print(change * -1);
    else:
        # print("Change Owed: ", end="");
        # print(change);
        print(f"Change Owed: {change}");


def subtract(change, coin):
    if coin == 25 or coin == 10 or coin == 5:
        total = change - coin;
    else:
        total = change;
    return (total);

main();
