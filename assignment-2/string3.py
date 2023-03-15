string = input("Enter a string: ")

# initializing counts
vowels = 0
digits = 0
consonants = 0
spaces = 0

# iterating through each character in the string
for char in string:
    if char.isalpha():
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

# printing the counts
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
