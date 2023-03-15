bin_num = input("Enter an 8-bit binary number: ")

# adding leading zeros if the length of bin_num is less than 8
bin_num = bin_num.zfill(8)

# converting binary number to hexadecimal
hex_num = hex(int(bin_num, 2))[2:]

# printing hexadecimal equivalent of the binary number
print("Hexadecimal equivalent:", hex_num.upper())
