def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=' ')

# Example usage
n = 10
print_fibonacci_series(n) # Output: 0 1 1 2 3 5 8 13 21 34
