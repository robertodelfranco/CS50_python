import sys

def shrink(string: str) -> None:
	print(string[:8])

def enlarge(string: str) -> None:
	i = len(string)
	while (i < 8):
		string += 'Z'
		i += 1
	print(string)

def main() -> None:
	if len(sys.argv) < 2:
		print("None")
		sys.exit(1)
	for arg in sys.argv[1:]:
		if len(arg) == 8:
			print(arg)
		elif len(arg) < 8:
			enlarge(arg)
		else:
			shrink(arg)


if __name__ == '__main__':
	main()