string = input("Enter a string: ")

# reversing the string
rev_string = string[::-1]

# checking if the reversed string is equal to the original string
if string == rev_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
