hex_num = input("Enter a two-digit hexadecimal number: ")

# converting hexadecimal number to decimal
dec_num = int(hex_num, 16)

# converting decimal number to binary
bin_num = bin(dec_num)[2:]

# printing decimal and binary equivalent of the hexadecimal number
print("Decimal equivalent:", dec_num)
print("Binary equivalent:", bin_num)
