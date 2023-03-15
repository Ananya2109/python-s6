password = input("Enter your password: ")

# initializing variables
contains_lower = False
contains_upper = False
contains_number = False
contains_special = False

# validating conditions
if len(password) >= 8:
    for char in password:
        if char.islower():
            contains_lower = True
        elif char.isupper():
            contains_upper = True
        elif char.isnumeric():
            contains_number = True
        elif char in ['$','#','@']:
            contains_special = True
    
    if contains_lower and contains_upper and contains_number and contains_special:
        print("Password is valid.")
    else:
        print("Password is invalid.")
else:
    print("Password is too short.")
