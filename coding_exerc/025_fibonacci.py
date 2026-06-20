
count = int(input("Enter the number of results you want to see: "))
result = []

for i in range(count):
    if i <= 1:
        result.append(1)
    else:
        result.append(result[i-1] + result[i-2])

print(result)       
