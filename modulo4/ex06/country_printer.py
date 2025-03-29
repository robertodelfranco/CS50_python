# import sys

def main() -> None:
	print_countries(name="Brazil", population="1230000", capital="Brasilia", currency="Real")
	print_countries(name="Germany", population="80000000", capital="Berlin", currency="Euro")
	print_countries(name="France", population="123000", capital="Paris", currency="Euro")
	print_countries(name="France", population="123", capital="Paris", currency="Euro")

def print_country_info(informations: dict) -> None:
	pop = int(informations['population'])
	if pop >= 1_000_000_000:
		informations['population'] = (pop / 1000000000)
		message = "{name} has a population of {population:g} billion. Its capital is {capital} and its currency is {currency}.".format(**informations)
	elif pop >= 1_000_000:
		informations['population'] = (pop / 1000000)
		message = "{name} has a population of {population:g} million. Its capital is {capital} and its currency is {currency}.".format(**informations)
	elif pop >= 1_000:
		informations['population'] = (pop / 1000)
		message = "{name} has a population of {population:g} thousand. Its capital is {capital} and its currency is {currency}.".format(**informations)
	else:
		message = "{name} has a population of {population}. Its capital is {capital} and its currency is {currency}.".format(**informations)
	print(message)
	return (message)

def create_country_dict(name: str, population: str, capital: str, currency: str) -> dict:
	country = {'name': name, 'population': population, 'capital': capital, 'currency': currency}
	return country

def print_countries(*arg: int, **kwargs: str) -> None:
	# args = {}
	# args.update(kwargs)
	# print(args)
	country_dict = create_country_dict(**kwargs)
	return(print_country_info(country_dict))



if __name__ == '__main__':
	main()