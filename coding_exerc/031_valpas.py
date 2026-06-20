base = input("Welcome to the password checker. \n The password must be between 6 and 16 characters long, contain at least one letter, one number, and one special character, and cannot contain spaces.\nEnter prospective password for validation:")

baseList = list(base)
alphaCount = 0
numCount = 0
specialCount = 0
minLength = 6
maxLength = 16



for i in range(len(baseList)):
    if baseList[i].isalpha():
        alphaCount += 1
    elif baseList[i].isdigit():
        numCount += 1
    elif baseList[i].isspace():
        print("Password cannot contain spaces.")
        break
    else:
        specialCount += 1

if minLength <= len(baseList) <= maxLength and alphaCount > 0 and numCount > 0 and specialCount > 0:
    print("Password is valid.")
else:
    print("Password doesn't meet the requirements.")