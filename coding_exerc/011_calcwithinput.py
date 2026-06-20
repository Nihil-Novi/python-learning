# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

while True:
    n = input("Give me a nuber. It can be a single digit or a multi-digit number: ")

    if not n.isdigit():
        print("I asked for a number, and that's not it.")
        continue

    print("The result is " + str(int(n) + int(n+n) + int(n+n+n)))