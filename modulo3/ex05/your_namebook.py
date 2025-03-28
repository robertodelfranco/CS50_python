

def main() -> None:
	persons = {
		"jean": "valjean",
		"grace": "hopper",
		"xavier": "niel",
		"fifi": "brindacier"
	}
	print(list_of_names(persons))


def list_of_names(person) -> str:
	names = []
	for first in person.keys():
		name = first
		names.append((name.title() + " " + person[name].title()))
	return names

main()