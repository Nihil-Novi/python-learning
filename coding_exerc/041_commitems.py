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

common_items = set1.intersection(set2)

if len(common_items) > 0:
    print("The common items in the two lists are: " + ", ".join(common_items))  
else:    print("There are no common items in the two lists.")   