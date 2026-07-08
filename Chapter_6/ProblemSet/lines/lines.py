# CITING https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
import os, sys

os.system("cls")


def main():
    if validateArguments():
        lines = getNumberOfLines()
        print(lines)

def validateArguments():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()

    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()

    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()

    else:
        return True


def getNumberOfLines():

    try:
        filename = sys.argv[1]
        with open(filename) as file:
            i = 0
            for line in file:
                if (
                    not line == "\n"
                    and not line.startswith("#")
                    and not line.startswith(" #")
                    and not line.startswith(" ")
                ):
                    i += 1
            return i

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


main()
