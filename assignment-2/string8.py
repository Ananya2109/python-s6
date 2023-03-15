string = input("Enter a string: ")

# initializing empty string for swapped case string
swapped_case = ""

# iterating through each character in string
for char in string:
    if char.isupper():
        # if character is uppercase, convert to lowercase and add to swapped_case
        swapped_case += char.lower()
    elif char.islower():
        # if character is lowercase, convert to uppercase and add to swapped_case
        swapped_case += char.upper()
    else:
        # if character is not a letter, add as it is
        swapped_case += char

# printing swapped case string
print("Swapped case string:", swapped_case)
