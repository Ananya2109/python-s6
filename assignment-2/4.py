# 4. Reverse a number and also find the sum of the digits
# Eg: i/p : 546 o/p:reverse=645 sum=15
num = int(input("Enter a number: "))


reverse_num = 0
while num > 0:
    remainder = num % 10
    reverse_num = (reverse_num * 10) + remainder
    num = num // 10


sum_of_digits = 0
for digit in str(reverse_num):
    sum_of_digits += int(digit)


print("Reverse:", reverse_num)
print("Sum of digits:", sum_of_digits)


