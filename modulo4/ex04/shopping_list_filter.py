import sys


def main() -> None:
	shopping_dict = {
		"banana": 10,
		"maçãs": 5,
		"laranja": 12,
		"kiwi": 24,
		"abacaxi": 1
	}
	amount = int(sys.argv[1])
	print(f"A lista de compras contém pelo menos {amount} dos seguintes itens:")
	for product in products_in_shopping_list(shopping_dict, amount):
		print(product)


def products_in_shopping_list(prod: dict, amount: int) -> dict:
	return {key: value for key, value in prod.items() if value >= amount}


main()