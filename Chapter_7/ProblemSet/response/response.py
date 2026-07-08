import validators


def main():
    email = getInput()
    result = validateEmail(email)
    print(result)
        

def getInput():
    userInput = input("What's your email address? ")
    return userInput
    

def validateEmail(email):
    result = validators.email(email) 
    
    if result == True:
        return "Valid"
    else:
        return "Invalid"
   
        
main()