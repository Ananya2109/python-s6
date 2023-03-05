#to find the binary equivalent of a number
num = int(input("Enter a number: "))

for digit in str(num):
    binary = ""
    quotient = int(digit)
    while quotient > 0:
        remainder = quotient % 2
        binary = str(remainder) + binary
        quotient = quotient // 2
    print(f"The binary equivalent of {digit} is {binary}")
