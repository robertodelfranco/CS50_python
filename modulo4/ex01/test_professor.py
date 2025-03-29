from help_your_professor import catch_median

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}

class_3C = {
 "quentin": 17,
 "julie": 15,
 "marc": 8,
 "stephanie": 13
}

def test_median():
	given = catch_median(class_3B)
	print(given)
	expected = 12.5
	assert given == expected


def test_median_again():
	given = catch_median(class_3C)
	print(given)
	expected = 13.25
	assert given == expected

