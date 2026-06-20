result = []
count = 0

for i in range(1500, 2700):
    if i %7 == 0 and i % 5 == 0:
        result.append(i)
        count += 1

choice = input("There are " + str(len(result)) + " numbers that are divisible by 5 and 7 between the range of 1500 and 2700.\n Would you like to display them? (Y/N) ")
if "Y":
    print(result)
else:
    print("Okay, be seeing you.")
