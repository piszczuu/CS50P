import os, sys
from PIL import Image, ImageOps

os.system("cls")


def main():

    if validateArguments(3):
        image = adjustImage(sys.argv[1])
        image.show()


def validateArguments(amountOfValidArguments):

    if len(sys.argv) > amountOfValidArguments:
        print("Too many command-line arguments")
        sys.exit()

    elif len(sys.argv) < amountOfValidArguments:
        print("Too few command-line arguments")
        sys.exit()

    elif not sys.argv[1].lower().endswith(".png") and not sys.argv[1].lower().endswith(
        ".jpg"
    ):
        print("Not a PNG or JPEG file")
        sys.exit()

    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        print("Arguments are not the same file type")
        sys.exit()

    else:
        return True


def adjustImage(image):
    photoId = getPhotoId(image)

    shirt = Image.open("shirt.png")
    shirtSize = shirt.size

    photo = Image.open(image)
    photo = ImageOps.fit(photo, shirtSize)
    photo.paste(shirt, shirt)

    newPhotoName = f"after{photoId}"
    photo.save(newPhotoName)

    return photo


def getPhotoId(image):

    try:
        photoId = image.split("before")
        photoId = photoId[1]

        return photoId

    except:
        sys.exit()


main()
