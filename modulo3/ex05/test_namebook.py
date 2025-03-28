from your_namebook import list_of_names


def test_list() -> None:
	given = list_of_names({
		"jean": "valjean",
		"grace": "hopper",
		"xavier": "niel",
		"fifi": "brindacier"
	})
	expected = ['Jean Valjean', 'Grace Hopper', 'Xavier Niel', 'Fifi Brindacier']
	assert expected == given