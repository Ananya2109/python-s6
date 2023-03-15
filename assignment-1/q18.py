#to check if a number is a krishnamurthi number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def is_krishnamurti(num):
    sum_of_factorials = 0
    for digit in str(num):
        sum_of_factorials += factorial(int(digit))
    if sum_of_factorials == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))


if is_krishnamurti(num):
    print(f"{num} is a Krishnamurti number.")
else:
    print(f"{num} is not a Krishnamurti number.")
