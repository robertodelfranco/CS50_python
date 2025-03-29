from transform import square_even_numbers

def test_one_number_odd():
	given = square_even_numbers([1])
	catch = []
	assert given == catch

def test_one_number_even():
	given = square_even_numbers([4])
	catch = [16]
	assert given == catch

def test_number_even():
	given = square_even_numbers([2, 4, 6, 7])
	catch = [4, 16, 36]
	assert given == catch