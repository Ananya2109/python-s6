def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] 
    return '0'*(4 - len(binary)) + binary if len(binary) < 4 else binary

def bcd_to_binary(number):
    result = ''
    for digit in str(number):
        result += decimal_to_binary(int(digit))
    return result

number = 15
binary = bcd_to_binary(number)
print(binary) 
