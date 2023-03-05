# 1. Print the sin series x-x^3/3!+x^5/5!....x^n/n! ( read n)
import math


x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))


result = 0
for i in range(n):
    sign = (-1) ** i
    term = x ** (2 * i + 1) / math.factorial(2 * i + 1)
    result += sign * term


print(result)

