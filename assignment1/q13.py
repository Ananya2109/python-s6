import math
#tofind the roots of a quadratic equation
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("The quadratic equation has no real roots.")
elif discriminant == 0:
    root = -b / (2*a)
    print("The quadratic equation has one root:", root)
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The quadratic equation has two roots:", root1, "and", root2)
