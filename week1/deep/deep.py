def main():
	str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip();
	conditionals(str);


def conditionals(str):
	match str:
		case "42" | "forty-two" | "forty two":
			print("Yes");
		case _:
			print("No");


main()


# number = number.strip().title()

# if number == "42":
#     print("Yes")
# elif number == "Forty Two" or number == "Forty-Two":
#     print("Yes")
# else:
#     print("No")
