def main():
	str = input('');
	convert(str);

def convert(str):
	str_new = str.replace(":)", "🙂");
	str_new2 = str_new.replace(":(", "🙁");
	print(str_new2);

main()

# sentence = input("")

# def main():
#     print(convert(sentence))


# def convert(sentence):
#     sentence = sentence.replace(":)", "🙂")
#     sentence = sentence.replace(":(", "🙁")

#     return sentence

# main()
