char = input("Enter a character: ")

if len(char) != 1:
    print("You can only enter one character.")
elif char.isalpha() and char.lower() in "aeiou":
    print("This is a vowel.")
elif char.isalpha() and char.lower() not in "aeiou":
    print("This is a consonant.")
else:
    print("This is not a letter, you can't use this one.")