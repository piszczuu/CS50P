import os, sys, csv

os.system("cls")


def main():
    
    if validateArguments(3):
        newDataList = getDictData()
        writeNewCSV(newDataList)


def validateArguments(amountOfValidArguments):
    
    if len(sys.argv) > amountOfValidArguments:
        print("Too many command-line arguments")
        sys.exit()

    elif len(sys.argv) < amountOfValidArguments:
        print("Too few command-line arguments")
        sys.exit()

    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

    else:
        return True


def getDictData():
    newDataList = []

    try:
        filename = sys.argv[1]
        with open(filename) as file:
            reader = csv.DictReader(file)
            tempDict = {}

            for row in reader:
                name = row["name"]
                house = row["house"]
                firstName, lastName = name.split(",")
                lastName = lastName.strip()

                tempDict["firstName"] = firstName
                tempDict["lastName"] = lastName
                tempDict["house"] = house

                newDataList.append(tempDict)
                tempDict = {}

        return newDataList

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


def writeNewCSV(newDataList):

    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["firstName", "lastName", "house"])

        for dict in newDataList:
            firstName = dict["firstName"]
            lastName = dict["lastName"]
            house = dict["house"]

            writer.writerow(
                {"firstName": firstName, "lastName": lastName, "house": house}
            )


main()
