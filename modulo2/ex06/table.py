import sys

def main() -> int:
	if (len(sys.argv) != 2 and len(sys.argv) != 1):
		print("Usage: python3 table.py or python3 table.py <number between 1 and 9>")
		sys.exit(1)
	try:
		if len(sys.argv) == 2:
			num = int(sys.argv[1])
			if (num >= 0 and num < 100):
				print_table_especific(num)
			else:
				print("Must be a number between 1 and 9")
				sys.exit(1)
		else:
			print_table()
			sys.exit(0)
	except ValueError:
		print("Usage: python3 table.py or python3 table.py <number between 1 and 9>")
		sys.exit(1)
	return (0)

def print_table() -> None:
	for i in range(0, 10):
		print(f"Table of {i}: ", end="")
		for j in range(0, 11):
			if (j == 10):
				print(f"{i * j}", end="")
			else:
				print(f"{i * j} ", end="")
		print("")

def print_table_especific(num: int) -> None:
	print(f"Table of {num}: ", end="")
	for i in range(1, 11):
		if (i == 10):
			print(f"{num * i}", end="")
		else:
			print(f"{num * i} ", end="")
	print("")

if __name__ == "__main__":
	sys.exit(main())