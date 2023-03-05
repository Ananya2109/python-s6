#to check if trinagle is valid and if it is a right angle triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))


if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle.")
else:
    
    sides = [a, b, c]
    sides.sort()

    
    if sides[0]*2 + sides[1]*2 == sides[2]*2:
        print("The triangle is a right triangle.")
    else:
        print("The triangle is not a right triangle.")
