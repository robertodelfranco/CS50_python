def main():
	dollars = dollars_to_float(input("How much was the meal? "));
	percent = percent_to_float(input("What percentage would you like to tip? "));
	tip = dollars * percent;
	print(f"Leave ${tip:.2f}");


def dollars_to_float(d):
	n = float(d.removeprefix("$"));

	return (n);


def percent_to_float(p):
	n = float(p.removesuffix("%"));
	n = n / 100;

	return (n);


main()


# def dollars_to_float(d):
#     d = float(d.replace("$", ""))

#     return d


# def percent_to_float(p):
#     p = float(p.replace("%", ""))
#     p = p / 100

#     return p