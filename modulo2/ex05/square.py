import sys

def main() -> int:
	if (len(sys.argv) != 2):
		print("Usage: python square.py <number between 0 and 50>")
		sys.exit(1)
	try:
		num = int(sys.argv[1])
		if (num >= 0 and num < 50):
			print_square(num)
		else:
			print("Must be a number between 0 and 50")
			sys.exit(1)
	except ValueError:
		print("Usage: python square.py <number between 0 and 50>")
		sys.exit(1)
	return (0)

def print_square(num: int) -> None:
	i = 0
	while (i < num):
		j = 0
		while (j < num):
			if i == 0 and j == 0 or i == num - 1 and j == 0 or i == 0 and j == num - 1 or i == num - 1 and j == num - 1:
				print("%", end="")
			elif i == 0 or i == num - 1:
				print("-", end="")
			elif j == 0 or j == num - 1:
				print("|", end="")
			else:
				print(" ", end="")
			j += 1
		print()
		i += 1


if __name__ == '__main__':
	sys.exit(main())