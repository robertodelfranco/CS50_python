import sys

def main():
	if (len(sys.argv) != 2):
		print("Usage: python3 multiplication_table.py <number>")
		exit(1)
	nb = sys.argv[1]
	for i in range(0, 11, 1):
		print(i, "x", nb, "=", int(nb) * i)


main()
