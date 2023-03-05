#to find absolute value of a number
def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n
n = float(input("Enter a number: "))
abs_value = absolute_value(n)
print("The absolute value of", n, "is", abs_value)

