import re, sys


def main():
    text = getInput()
    result = count(text)
    print(result)


def getInput():
    userInput = input("Input: ")
    return userInput


def count(text):
    umList = re.findall(r"\bum\b", text, flags=re.IGNORECASE)
    numOfUms = len(umList)
    return numOfUms


if __name__ == "__main__":
    main()
