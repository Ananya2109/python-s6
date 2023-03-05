#to find dec binary and oct equivalent of hexa number
hex_number = input("Enter a hexadecimal number: ")
dec_number = int(hex_number, 16)
bin_number = bin(dec_number)
oct_number = oct(dec_number)
print("Decimal equivalent:", dec_number)
print("Binary equivalent:", bin_number)
print("Octal equivalent:", oct_number)
