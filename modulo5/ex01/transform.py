#!/usr/bin/env python3
def f_square(nb):
	return nb * nb

def is_even(nb):
	return nb % 2 == 0

def square_even_numbers(list_of_ints: list) -> list:
	evens = filter(is_even, list_of_ints)
	list_of_evens = list(evens)
	if list_of_evens == []:
		print(list_of_evens)
		return []
	squares = map(f_square, list_of_evens)
	list_of_squares = list(squares)
	print(list_of_squares)
	return list_of_squares


square_even_numbers([1])
square_even_numbers([4])
square_even_numbers([2, 4, 6, 7])