def main():
    word = input("Input: ");
    print("Output: ", end="");
    print(shorten(word))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    result = []
    for char in word:
        if char not in vowels:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    main()
