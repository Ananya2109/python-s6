dec_num = int(input("Enter a decimal number: "))

# initializing empty string for binary representation
bin_num = ""

# dividing the decimal number by 2 and appending the remainder to bin_num string
while dec_num > 0:
    bin_num = str(dec_num % 2) + bin_num
    dec_num //= 2

# printing binary representation of the decimal number
print("Binary representation:", bin_num)
