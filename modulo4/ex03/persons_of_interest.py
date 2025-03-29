
def main() -> None:
	women_scientists = {
		"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
		"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
		"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
		"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
	}
	famous_births(women_scientists)


def famous_births(womens: dict) -> list:
	list_of_peoples = []
	for key_master in womens.keys():
		list_of_peoples.append(womens[key_master])
		for key in womens[key_master]:
			if key == 'date_of_birth':
				nb = int(womens[key_master][key])
				womens[key_master][key] = nb
	new_womens = dict(sorted(womens.items(), key=lambda item: item[1]['date_of_birth']))
	for women in new_womens.keys():
		print(f"{new_womens[women]['name']} is a great scientist born in {new_womens[women]['date_of_birth']}")


if __name__ == '__main__':
	main()