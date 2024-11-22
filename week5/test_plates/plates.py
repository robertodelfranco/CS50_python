def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if 'A' <= s[0] <= 'Z' and 'A' <= s[1] <= 'Z':
            if len(s) > 2:
                flag = 0;
                for i in range(2, len(s)):
                    if 'A' <= s[i] <= 'Z' and flag == 0:
                        continue;
                    elif '1' <= s[i] <= '9' and flag == 0:
                        flag = 1;
                    elif '0' <= s[i] <= '9' and flag == 1:
                        continue;
                    elif 'A' <= s[i] <= 'Z' and flag == 1:
                        return False;
                    else:
                        return False;


                return True;
            else:
                return True;
        else:
            return False;
    else:
        return False;


if __name__ == "__main__":
    main()
