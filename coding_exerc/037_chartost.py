print("Enter bunch of characters to be conversted into a list. Press ''enter'' after each one. When you are done, just press ''enter'' without typing anything.")
result = []

while True:
    char = input("Enter a character: ")
    if char == "":
        break
    else:
        result.append(char)
        continue

print("The string you entered is: " + "".join(result))