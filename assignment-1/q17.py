# to check if the number is an Armstrong number
num = int(input("Enter a 3-digit number: "))


digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10


sum_cubes = digit1*3 + digit2*3 + digit3*3

if sum_cubes == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")