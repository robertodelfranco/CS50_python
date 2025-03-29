str = input("Input: ");

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

print("Output: ", end="");
for char in str:
    if char in vowels:
        continue;
    print(char, end="");


print();
