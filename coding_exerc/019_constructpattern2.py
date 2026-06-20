#  Write a Python program to construct the following pattern, using a nested for loop.

j=1
for i in range (11):
    while i<=5:
        print(str("*")*j)
        j+=1
        break
    while i>5:
        print(str("*")*j)
        j-=1
        break