def main():
	list = input("Expression: ").split();
#	x, y, z = input("Expression: ").split(" ");

	x = float(list[0]);
	y = list[1];
	z = float(list[2]);
	result = inCase(x, y, z);

	print(result);


def inCase(x, y, z):
	if y == '+':
		return (x + z);
	elif y == '-':
		return (x - z);
	elif y == '*':
		return (x * z);
	elif y == '/' and z != 0:
		return (x / z);
	elif y == '/' and z == 0:
		return ("z can't be zero");


main()


# def main():
#     x, y, z = input("Expression: ").split(" ")


#     if y == ("+"):
#         a = float(x) + float(z)
#         print(a)
#     elif y == ("-"):
#         b = float(x) - float(z)
#         print(b)
#     elif y == ("*"):
#         c = float(x) * float(z)
#         print(c)
#     elif y == ("/") and z != "0":
#         d = float(x) / float(z)
#         print(d)
#     elif y == ("/") and z == "0":
#         print("z can't be zero")