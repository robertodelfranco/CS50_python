from letter_histogram import histogram


# def test_list_receive():
# 	given = histogram("abacate")
# 	expected = ['a', 'b', 'a', 'c', 'a', 't', 'e']
# 	assert expected == given


# def test_list_sort():
# 	given = histogram("casa")
# 	expected = ['a', 'c', 's']
# 	assert expected == given

def test_dict_sort():
	given = histogram("casa")
	expected = {'a': '**', 'c': '*', 's': '*'}
	assert given == expected