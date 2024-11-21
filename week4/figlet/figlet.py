import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 3 and sys.argv[1] == "-f" and sys.argv[2] in fonts:
    catch = pyfiglet.Figlet(font=sys.argv[2]);

    str = input("Input: ");

    fontstr = catch.renderText(str)
    print("Output:" )
    print(fontstr);
elif len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    catch = pyfiglet.Figlet(font=random_font)

    str = input("Input: ");

    fontstr = catch.renderText(str)
    print("Output:" )
    print(fontstr);
else:
    sys.exit("Invalid usage")
