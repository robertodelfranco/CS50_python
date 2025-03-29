from country_printer import print_country_info, print_countries


def test_country_info():
	given = print_country_info({'name': "Germany", 'population': "80", 'capital': "Berlin", 'currency': "Euro"})
	catch = "Germany has a population of 80. Its capital is Berlin and its currency is Euro."
	assert given == catch


def test_print_countries():
	given = print_countries(name="France", population="123", capital="Paris", currency="Euro")
	catch = "France has a population of 123. Its capital is Paris and its currency is Euro."
	assert given == catch


def test_print_thousand():
	given = print_countries(name="France", population="123000", capital="Paris", currency="Euro")
	catch = "France has a population of 123 thousand. Its capital is Paris and its currency is Euro."
	assert given == catch



def test_print_million():
	given = print_countries(name="Brazil", population="1230000", capital="Brasilia", currency="Real")
	catch = "Brazil has a population of 1.23 million. Its capital is Brasilia and its currency is Real."
	assert given == catch