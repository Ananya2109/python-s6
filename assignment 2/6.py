
# 6. Find the square root of a number using Newton’s method ( refer the text book/blog for reference)
n = float(input("Enter a number: "))


guess = n / 2
tolerance = 0.0001


while abs(guess ** 2 - n) > tolerance:
    guess = (guess + n / guess) / 2


print("The square root of", n, "is", guess)

