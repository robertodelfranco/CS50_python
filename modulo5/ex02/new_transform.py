#!/usr/bin/env python3

def f_square(nb):
	return nb * nb

def is_even(nb):
	return nb % 2 == 0

def square_even_numbers(list_of_ints: list) -> list:
	return [n * n for n in list_of_ints if n % 2 == 0]

square_even_numbers([1])
square_even_numbers([4])
square_even_numbers([2, 4, 6, 7])