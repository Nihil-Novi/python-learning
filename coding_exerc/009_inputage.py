# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import datetime

currentYear = int(datetime.now().strftime("%Y"))

while True:
    print("Let's see something real quick.")
    age = input("When were you born? Just the number will suffice. ")

    if not age.isdigit():
        print("Nuh-uh. THat's not a number")
        

        continue

    print("You're " + str(int(currentYear) - int(age)) + " years old. You'll be 100 in " + str(int(age) + 100))

                