#8.  Check whether the given number is a Krishnamurti number(.Use factorial() function from math)
#For example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145 is a Krishnamurthy Number
import math


n = int(input("Enter a number: "))
digits = str(n)
fact_sum = sum([math.factorial(int(digit)) for digit in digits])
if fact_sum == n:
    print(f"{n} is a Krishnamurti number")
else:
    print(f"{n} is not a Krishnamurti number")

