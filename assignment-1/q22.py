#to find the square root of first and last digits of a number
import math

n = int(input("Enter a number: "))

first_digit = n
while first_digit >= 10:
    first_digit //= 10
last_digit = n % 10

sqrt_first = math.sqrt(first_digit)
sqrt_last = math.sqrt(last_digit)

print(
    f"The square root of the first digit ({first_digit}) is {sqrt_first:.2f}.")
print(f"The square root of the last digit ({last_digit}) is {sqrt_last:.2f}.")
