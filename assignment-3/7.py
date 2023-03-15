str=input("Enter the string: ")
words=str.split(" ")
words.sort()
print("words in alphabetical order:",*words)