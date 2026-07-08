import re
import sys
import random, os
from time import sleep

os.system("cls")


def main():
    time = getInput()
    # print(time)
    format = chooseFormat(time)
    result = convertFormat(format, time)
    print(result)


def getInput():
    userInput = input("Hours: ")
    return userInput


def chooseFormat(time):

    # 9:00 AM to 5:00 PM
    if re.search(r"^(\d{1,2}):(\d\d) AM to (\d{1,2}):(\d\d) PM$", time):
        format = "format1"

    # 9 AM to 5 PM
    elif re.search(r"^\d{1,2} AM to \d{1,2} PM$", time):
        format = "format2"

    # 9:00 AM to 5 PM
    elif re.search(r"^\d{1,2}:\d\d AM to \d{1,2} PM$", time):
        format = "format3"

    # 9 AM to 5:00 PM
    elif re.search(r"^\d{1,2} AM to \d{1,2}:\d\d PM$", time):
        format = "format4"

    else:
        return False

    return format


def convertFormat(format, time):

    match format:

        case "format1":
            if matches := re.search(
                r"^(\d{1,2}):(\d\d) AM to (\d{1,2}):(\d\d) PM$", time
            ):
                fromHour = matches.group(1)
                fromMinute = matches.group(2)
                toHour = matches.group(3)
                toMinute = matches.group(4)

                newFormat = f"{fromHour}:{fromMinute} to {toHour}:{toMinute}"
                return newFormat

        case "format2":
            if matches := re.search(r"^(\d{1,2}) AM to (\d{1,2}) PM$", time):
                fromHour = matches.group(1)
                toHour = matches.group(2)

                newFormat = f"{fromHour}:00 to {toHour}:00"
                return newFormat

        case "format3":
            if matches := re.search(r"^(\d{1,2}):(\d\d) AM to (\d{1,2}) PM$", time):
                fromHour = matches.group(1)
                fromMinute = matches.group(2)
                toHour = matches.group(3)

                newFormat = f"{fromHour}:{fromMinute} to {toHour}:00"
                return newFormat

        case "format4":
            if matches := re.search(r"^(\d{1,2}) AM to (\d{1,2}):(\d\d) PM$", time):
                fromHour = matches.group(1)
                toHour = matches.group(2)
                toMinute = matches.group(3)

                newFormat = f"{fromHour}:00 to {toHour}:{toMinute}"
                return newFormat

        case _:
            # print("Error")
            sys.exit()


if __name__ == "__main__":
    main()
