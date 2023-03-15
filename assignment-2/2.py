# 2. In the above program read the value x and find the sum of the series.
import math


x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))


result = 0
for i in range(n):
    sign = (-1) ** i
    term = x ** (2 * i + 1) / math.factorial(2 * i + 1)
    result += sign * term


print("The sum of the series is:", result)




