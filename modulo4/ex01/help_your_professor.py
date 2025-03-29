class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}

def main() -> None:
	print(catch_median(class_3B))


def catch_median(students: dict) -> float:
	i = 0;
	median = 0.0
	for notas in students.values():
		median += float(notas)
		i += 1
	return (median / i)


if __name__ == '__main__':
	main()