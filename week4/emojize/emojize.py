import emoji

str = input("Input: ");

print("Output: ", end="");

print(emoji.emojize(str, language="alias"));