import sys

def main() -> None:
	if len(sys.argv) == 1:
		print("None")
		sys.exit(1)
	for arg in sys.argv[1:]:
		print(downcase_it(arg))


def downcase_it(string: str) -> str:
	return string.lower()

if __name__ == "__main__":
	main()