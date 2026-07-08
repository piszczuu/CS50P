import os, tabulate, sys, csv

os.system("cls")


def main():
    if validateArguments():
        headers, table = getDictInfo()
        print(tabulate.tabulate(table, headers, tablefmt="grid"))


def validateArguments():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()

    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()

    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

    else:
        return True


def getDictInfo():
    headers = []
    table = []

    try:
        filename = sys.argv[1]
        with open(filename) as file:
            reader = csv.DictReader(file)
            tempList = []

            for row in reader:

                for key in row:
                    value = row.get(key)

                    if len(headers) < 3:
                        headers.append(key)

                    tempList.append(value)

                table.append(tempList)
                tempList = []

            return headers, table

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


main()
