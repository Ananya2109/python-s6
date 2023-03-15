#to find details of a cordinate
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

if x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point is on the y-axis.")
elif y == 0:
    print("The point is on the x-axis.")
elif x > 0 and y > 0:
    print("The point is in the first quadrant.")
elif x < 0 and y > 0:
    print("The point is in the second quadrant.")
elif x < 0 and y < 0:
    print("The point is in the third quadrant.")
else:
    print("The point is in the fourth quadrant.")
