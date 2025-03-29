def main() -> None:
	greetings('Bob')
	greetings('Alice')
	greetings()
	greetings(24)


def greetings(string: str = "pessoa desconhecida") -> None:
	if not isinstance(string, str):
		print("Error: argumento inválido")
		return
	print(f"Hello, {string}.")


if __name__ == "__main__":
	main()