import sys

def main() -> None:
	if len(sys.argv) < 2:
		print("Error: give at least one argument")
		sys.exit(1)
	elif len(sys.argv) >2:
		print("Error: give just one argument")
		sys.exit(1)
	try:
		with open(sys.argv[1], 'r') as file:
			readfile(file)
	except Exception as e:
		print(f"Error: {type(e).__name__}")


def readfile(file: object) -> str:
	conteudo = file.read()
	print(conteudo)
	return (conteudo)

if __name__ == '__main__':
	main()