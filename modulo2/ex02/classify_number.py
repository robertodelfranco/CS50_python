import sys

def main():
	if (len(sys.argv) != 2):
		print("Usage: python classify_number.py <number>")
		sys.exit(1)
	try:
		num = int(sys.argv[1])
	except ValueError:
		print("Usage: python classify_number.py <number>")
		sys.exit(1)
	is_even = even_or_odd(num)
	is_positive = positive_or_negative(num)
	if (num == 0):
		print("zero")
	elif (is_even and is_positive):
		print("positive and even")
	elif (is_even and not is_positive):
		print("negative and even")
	elif (not is_even and is_positive):
		print("positive and odd")
	else:
		print("negative and odd")

def even_or_odd(num: int) -> bool:
	if (num % 2 == 0):
		return True
	else:
		return False

def positive_or_negative(num: int) -> bool:
	if (num > 0):
		return True
	else:
		return False 

if __name__ == '__main__':
	main()