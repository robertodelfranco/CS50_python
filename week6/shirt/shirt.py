import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].endswith((".jpg", ".jpeg",".png")):
        sys.exit("Invalid input")
    file_one = sys.argv[1].rsplit(".", 1)[-1]
    file_two = sys.argv[2].rsplit(".", 1)[-1]
    if file_one != file_two:
        sys.exit("Input and output have different extensions")
    try:
        with Image.open(sys.argv[1]) as image:
            with Image.open("shirt.png") as shirt:
                image = ImageOps.fit(image, shirt.size)
                image.paste(shirt, (0, 0), shirt)
                image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == '__main__':
    main()
