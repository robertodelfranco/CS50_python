

def main():
	histogram('casa')

def histogram(string: str) -> dict:
	list_of_chars = list(string)
	list_of_chars.sort()
	dict_of_chars = dict.fromkeys(list_of_chars)
	list_without_rep = list(dict_of_chars)
	c = 0
	i = 0
	while c < len(list_without_rep):
		freq = 0
		while i < len(list_of_chars):
			if list_of_chars[i] == list_without_rep[c]:
				freq += 1
			i += 1
		if freq == 0:
			freq += 1
		dict_of_chars[list_without_rep[c]] = '*' * freq
		c += 1
	print(dict_of_chars)
	return(dict_of_chars)

if __name__ == '__main__':
	main()