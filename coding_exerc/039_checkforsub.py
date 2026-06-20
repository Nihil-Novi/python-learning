print("Enter the list to be searched for a substring. Press ''enter'' after each one. When you are done, just press ''enter'' without typing anything.")
searchable = []
sublist = []

while True:
    element = input("Enter an element: ")
    if element != "":
        searchable.append(element)
    else:
        break

print("Enter the sublist you want to search for. The rules are the same, hit ''enter'' after every entry and hit ''enter'' again if you want to finish: ")
while True:
    element = input("Enter an element: ")
    if element != "":
        sublist.append(element)
    else:
        break
    
if set(sublist).issubset(set(searchable)):
     print("The sublist is in the list.")
else:
    print("The sublist is not in the list.")

