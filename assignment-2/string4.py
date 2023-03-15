bin_num = input("Enter a binary number: ")

# initializing decimal number to 0
dec_num = 0

# iterating through each character in the binary number string
for i in range(len(bin_num)):
    # converting character to integer and adding to decimal number
    dec_num += int(bin_num[i]) * 2 ** (len(bin_num) - i - 1)

# printing decimal equivalent of the binary number
print("Decimal equivalent:", dec_num)
