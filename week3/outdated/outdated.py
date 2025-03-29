

def main():
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    while True:
        try:
            str = input("Date: ");
            if any(str.startswith(month) for month in months_list):
                if str.find(",") != -1: # if "," in str:
                    newstr = str.replace(",", "");
                    month, day, year = newstr.split(" ");
                    if 0 < int(day) <= 31 and int(year) > 0:
                        get_date(months_list, day, month, year);
                        break
            else:
                month, day, year = str.split("/");
                if 0 < int(day) <= 31 and 0 < int(month) <= 12 and int(year) > 0:
                    reverse_date(int(day), int(month), int(year))
                    break
        except ValueError:
            pass


def get_date(months_list, day, month, year):
    newmonth = (months_list.index(month) + 1);
    reverse_date(int(day), int(newmonth), int(year));


def reverse_date(day, month, year):
    print(f"{year}-{month:02}-{day:02}");


main()
