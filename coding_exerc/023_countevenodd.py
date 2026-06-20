numbers = tuple(input("Enter a string of numbers: ").split())
evenCount = 0
oddCount = 0

for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print("This string contains " + str(evenCount) + " even numbers and " + str(oddCount) + " odd numbers.")