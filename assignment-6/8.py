import getpass

password=getpass.getpass("password: ")
if(len(password)<6):
    print("password is too short")
    exit()
if(password.isupper()):
    print("password must contain lower case characters")
    exit()
if(password.islower()):
    print("password must contain upper case characters")
    exit()
if(password.isalnum()):
    print("password must contain special characters")
    exit()
if(password.isalpha()):
    print("password must contain numbers")
    exit()
print("password is strong")