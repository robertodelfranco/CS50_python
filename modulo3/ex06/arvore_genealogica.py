import sys

def main() -> None:
	if len(sys.argv) != 2:
		sys.exit("Just one argument")
	familia_silva = {
		"João": {
		"pais": ["Maria", "Pedro"],
		"nascimento": 1980,
		"cidade": "São Paulo"
		},
		"Maria": {
		"pais": ["Ana", "Carlos"],
		"nascimento": 1955,
		"cidade": "Rio de Janeiro"
		},
		"Pedro": {
		"pais": ["Beatriz", "José"],
		"nascimento": 1953,
		"cidade": "Belo Horizonte"
		},
		"Ana": {
		"pais": ["Francisca", "Antônio"],
		"nascimento": 1930,
		"cidade": "Salvador"
		},
		"Carlos": {
		"pais": [],
		"nascimento": 1928,
		"cidade": "Recife"
		},
		"Beatriz": {
		"pais": ["Helena", "Manuel"],
		"nascimento": 1925,
		"cidade": "Fortaleza"
		},
		"José": {
		"pais": [],
		"nascimento": 1923,
		"cidade": "Porto Alegre"
		}
	}
	print(encontrar_ancestrais(familia_silva, sys.argv[1]))


ancestrais = []

def encontrar_ancestrais(dict: dict, key: str) -> list:
	if key not in dict:
		return []
	if key in dict:
		parents = dict[key]['pais']
		if len(parents) > 1:
			if parents[0] != [] and parents[0] not in ancestrais and parents[1] != [] and parents[1] not in ancestrais:
				ancestrais.extend(parents)
			if len(ancestrais) >= 4:
				if ancestrais[0] in dict and ancestrais[1] in dict:
					if not any(pai in ancestrais for pai in dict[ancestrais[1]]['pais']):
						encontrar_ancestrais(dict, ancestrais[1])
				if ancestrais[2] in dict and ancestrais[3] in dict:
					if not any(pai in ancestrais for pai in dict[ancestrais[2]]['pais']):
						encontrar_ancestrais(dict, ancestrais[2])
			encontrar_ancestrais(dict, parents[0])
			encontrar_ancestrais(dict, parents[1])
	return ancestrais


if __name__ == '__main__':
	main()

