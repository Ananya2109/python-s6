#to find largest and smallest number among 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("The largest number is:", largest)
print("The smallest number is:", smallest)
