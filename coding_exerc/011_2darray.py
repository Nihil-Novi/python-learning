# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 

while True:
    m = input("How many rows should the array have? ")
    if not m.isdigit():
        print("That's not a number. Once again, from the top.\n")
        continue
    n = input("How many columns should the array have? ")
    if not n.isdigit():
        print("That's not a number. Once again, from the top.\n")
        continue

    for i in range (int(m)):
        row = []
        for j in range (int(n)):
            row.append(i*j)
        print(row)