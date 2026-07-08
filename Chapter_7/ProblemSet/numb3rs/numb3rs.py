import re
import sys


def main():
    address = getInput()
    status = validate(address)
   
    if not status:
        sys.exit()
    elif status == True:
        sys.exit()
    elif status == False:
        sys.exit()
        

def getInput():
    userInput = input("IPv4 Address: ").strip()
    return userInput


def validate(address):
    try:
        blocks = address.split(".")
    except:
        # print("cant split")
        return False
        
    for block in blocks: 
        if re.search(r"^(0\d*)$", block):
            # print("detected leading zero")
            return False

    if re.search(
        r"^([0-255]{1,3})\.([0-255]{1,3})\.([0-255]{1,3})\.([0-255]{1,3})$", address
    ):
        return True

    else:
        # print("bad range")
        return False


if __name__ == "__main__":

    try:
        main()
    except:
        sys.exit()
