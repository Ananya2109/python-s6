import math
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def cos_series(x, n):
    sum = 1
    sign = -1
    for i in range(1, n+1):
        term = sign * (x**(2*i)) / fact(2*i)
        sum += term
        sign *= -1
    return sum

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms to use: "))

result = cos_series(x, n)
print("The sum of the cosine series up to {} terms is: {}".format(n, result))
