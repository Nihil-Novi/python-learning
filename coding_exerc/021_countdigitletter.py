# Write a Python program that accepts a string and calculate the number of digits and letters

base = input("Enter a bit of text: ")
baseList = list(base)
alphaCount = 0
numCount = 0
spaceCount = 0
otherCount = 0

for i in range(len(baseList)):
    if baseList[i].isalpha():
        alphaCount += 1
    elif baseList[i].isdigit():
        numCount += 1
    elif baseList[i].isspace():
        spaceCount += 1
    else:
        otherCount += 1

print("This text contains " + str(alphaCount) + " letters, " + str(numCount) + " numbers, " + str(spaceCount) + " spaces, and " + str(otherCount) + " other characters.")