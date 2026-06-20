print("Let's make a list. First, enter the items in the first list. Press ''enter'' after each one. When you are done, just press ''enter'' without typing anything.")
list = []
while True:
    item = input("Enter an item: ")
    if item != "":
        list.append(item)
    else:
        break

for i in range(len(list)):
    list[i] = int(list[i])

max_item = max(list)

print("The maximum item in the list is: " + str(max_item))
