from datetime import datetime

currentYear = int(datetime.now().strftime("%Y"))

while True:
    print("Let's see something real quick.")
    age = input("When were you born? Just the number will suffice. ")

    if not age.isdigit():
        print("Nuh-uh. THat's not a number")
        

        continue

    print("You're " + str(int(currentYear) - int(age)) + " years old. Yeah, that checks out.\n")

                