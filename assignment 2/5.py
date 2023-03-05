# 5. Positive integer is called an Armstrong number of order n if
#abcd…. = a ^ n + b ^ n + c ^ n + d ^ n + where n is the length of the number
#Eg: 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong Number.
#Eg: 1634 = 1**4+6**4+3**4+4**4 = 1634 // 1634 is an Armstrong Number.
num = int(input("Enter a positive integer: "))
order = len(str(num))
sum = 0


temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10


if num == sum:
   print(num, "is an Armstrong number!")
else:
   print(num, "is not an Armstrong number.")


