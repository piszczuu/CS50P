import re
import sys


def main():
    input = getInput()
    print(parseURL(input))


def getInput():
    userInput = input("URL: ").strip()
    return userInput


def parseURL(url):

    if matches := re.search(
        r"https?://(?:www\.)?youtube\.com/embed/(\w+)", url, re.IGNORECASE
    ):
        code = matches.group(1)
        newURL = f"https://youtu.be/{code}"
        return newURL

    else:
        return None


if __name__ == "__main__":
    main()
