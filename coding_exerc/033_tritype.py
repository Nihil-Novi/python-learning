a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))

if a == b and b == c:
    print("This is an equilateral triangle.")
elif a != b and b != c and c != a and a + b > c and a + c > b and b + c > a:
    print("This is a scalene triangle.")
elif a == b or b == c or c == a:
    print("This is an isosceles triangle.")
else:
    print("This is not a triangle, these walls won't meet up to form a closed shape.")
