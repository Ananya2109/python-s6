#to find sum of digits using recursion
def recursive_digit_sum(n):

    if n < 10:
        return n
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return recursive_digit_sum(digit_sum)


n = int(input("Enter a number: "))
print("The recursive digit sum of", n, "is", recursive_digit_sum(n))
