print("Let's make two lists. First, enter the items in the first list. Press ''enter'' after each one. When you are done, just press ''enter'' without typing anything.")
list1 = []
while True:
    item = input("Enter an item: ")
    if item != "":
        list1.append(item)
    else:
        break

print("Now, enter the items in the second list. The rules are the same, hit ''enter'' after every entry and hit ''enter'' again if you want to finish: ")
list2 = []
while True:
    item = input("Enter an item: ")
    if item != "":
        list2.append(item)
    else:
        break

set1 = set(list1)
set2 = set(list2)

set3 = (set1 - set2).union(set2 - set1)
if len(set3) > 0:
    print("The differences are: " + ", ".join(set3))