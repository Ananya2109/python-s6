def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Example usage
n = 12345
result = sum_of_digits(n)
print(result) # Output: 15
