def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r):
    if r > n:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n-r))

n = 7
r =4
result = nCr(n, r)
print(result)
