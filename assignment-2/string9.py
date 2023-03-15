message = input("Enter message to encrypt: ")

# initializing empty string for encrypted message
encrypted_message = ""

# iterating through each character in message
for char in message:
    # shifting character by 3 positions
    if char.isupper():
        # if character is uppercase
        encrypted_message += chr((ord(char) + 3 - 65) % 26 + 65)
    elif char.islower():
        # if character is lowercase
        encrypted_message += chr((ord(char) + 3 - 97) % 26 + 97)
    else:
        # if character is not a letter, add as it is
        encrypted_message += char

# printing encrypted message
print("Encrypted message:", encrypted_message)
