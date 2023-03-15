#to find are of circle using points
import math
xc = float(input("Enter the x-coordinate of the center: "))
yc = float(input("Enter the y-coordinate of the center: "))
x1 = float(input("Enter the x-coordinate of the point on the circumference: "))
y1 = float(input("Enter the y-coordinate of the point on the circumference: "))
radius = math.sqrt((x1 - xc) * 2 + (y1 - yc) * 2)
area = math.pi * radius ** 2
print("The area of the circle is:", area)
