import sys

def main() -> int:
	if (len(sys.argv) != 2):
		print("Usage: python fibonacci.py <number>")
		sys.exit(1)
	try:
		num = int(sys.argv[1])
		if (num > -1 and num < 10):
			print(fibonacci(num))
		else:
			print("Must be a number between 0 and 9")
			sys.exit(1)
	except ValueError:
		print("Usage: python fibonacci.py <number>")
		sys.exit(1)
	return (0)


def fibonacci(num: int) -> int:
	i = 0
	array = []
	while (i < 10):
		if i == 0:
			array.append(0)
		elif i == 1:
			array.append(1)
		else:
			array.append(array[i - 1] + array[i - 2])
		i += 1
	return array[num]


if __name__ == '__main__':
	sys.exit(main())