
#9.  Find the sum of the first and last digit of a number(i/p: 345 o/p=3+5=8)
n = input("Enter a number: ")
first_digit = int(n[0])
last_digit = int(n[-1])
sum_of_digits = first_digit + last_digit
print(f"The sum of the first and last digit of {n} is {sum_of_digits}")
