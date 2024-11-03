def main():
	str = input("Greeting: ").strip();
	conditionals(str);


def conditionals(str):
		if str.startswith("Hello") or str.startswith("hello"):
			print("$0");
		elif str.startswith("H") or str.startswith("h"):
			print("$20");
		else:
			print("$100");


main()


# def main():
#     name = input("Gretting: ").strip().title()

#     if name.startswith("Hello"):
#         print("$0")
#     elif name.startswith("H"):
#         print("$20")
#     else:
#         print("$100")