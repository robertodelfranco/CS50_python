import sys
import chardet

def main() -> None:
	if len(sys.argv) < 2:
		print("Error: give just two arguments")
		sys.exit(1)
	try:
		with open(sys.argv[1], 'rb') as file:
			conteudo = file.read()
			result = chardet.detect(conteudo)
			encoding = result['encoding']
			readfile(sys.argv[1], encoding, sys.argv[2])
	except Exception as e:
		print(f"Error: {type(e).__name__}")


def readfile(file: object, encod: str, name: str) -> str:
	with open(file, 'r', encoding=encod) as f:
		conteudo = f.read()
	with open(name, 'x', encoding='utf-8') as final_file:
		final_file.write(conteudo)
	print("Arquivo 'utf-8_encoded.txt' criado com sucesso.")
	return (final_file)

if __name__ == '__main__':
	main()