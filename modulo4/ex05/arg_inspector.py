

def inspect_arguments(*args: int, **kwargs: str) -> dict:
	# if not args and not kwargs:
	# 	return print(None)
	# i = 0
	# list_of_args = []
	# list_of_index = []
	# for arg in args:
	# 	list_of_index.append(i)
	# 	list_of_args.append(arg)
	# 	i += 1
	dict_of_args = {} # dict.fromkeys(list_of_index)
	print(kwargs)
	# j = 0
	# for key in dict_of_args.keys():
	# 	dict_of_args[key] = list_of_args[j]
	# 	j += 1
	dict_of_args.update(kwargs)
	print(dict_of_args)


inspect_arguments(42, "hello", True, name="Alice", age=30, language="Python")
inspect_arguments()
inspect_arguments(1, 2, 3)
inspect_arguments(city="Paris", country="France")