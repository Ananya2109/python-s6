# Define the string
str = "Python Programming by Yourname"

# a) To display the last four characters
print(str[-4:])

# b) To display the substring starting from index 4 and ending at index 8
print(str[4:9])

# c) Find the length of the string, min and max(characters)
print("Length of the string:", len(str))
print("Minimum character:", min(str))
print("Maximum character:", max(str))

# d) To trim the last four characters from the string
print(str[:-4])

# e) To trim the first four characters from the string
print(str[4:])

# f) To display the starting index of the substring 'gr'
print(str.find('gr'))

# g) To change the case of the given string.( small letter to capital and capital to small)
print(str.swapcase())

# h) To check if the string is in title case
print(str.istitle())

# i) To replace all the occurrences of letter 'm' in the string with '*'
print(str.replace('m', '*'))

# j) Reverse the string
print(str[::-1])

# k) Count the occurrence of the character ‘m’
print(str.count('m'))

# l) Characters in even positions 0, 2, 4, ......
print(str[::2])

# m) Characters in even positions 0, 2, 4, .....in reverse order
print(str[::-2])

# n) Check whether the substring ‘on’ is present in the string or not
print('on' in str)

# o) Find the first occurrence of character ‘t’
print(str.index('t'))

# p) Convert the string into upper case
print(str.upper())
