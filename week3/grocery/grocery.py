

def main():
    dict = {};
    while True:
        try:
            str = input("").upper();
            update_dict(dict, str);
        except EOFError:
            break;

    ft_print(dict);

def update_dict(dict, key):
    if key in dict:
        dict[key] += 1;
    else:
        dict[key] = 1;


def ft_print(dict):
    for key in sorted(dict.keys()):
        print(dict[key], key);


main()
