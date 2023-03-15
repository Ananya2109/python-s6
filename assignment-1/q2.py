#to find last 2 digits of phone number and find its vinary octal and hexa representations
phone_number = input("Enter your phone number: ")
last_two_digits = phone_number[-2:]
binary = bin(int(last_two_digits))
octal = oct(int(last_two_digits))
hexadecimal = hex(int(last_two_digits))
print("Last two digits of the phone number:", last_two_digits)
print("Binary representation:", binary)
print("Octal representation:", octal)
print("Hexadecimal representation:", hexadecimal)
