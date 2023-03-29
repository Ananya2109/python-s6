string = input("Enter a string: ")

char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Frequency of occurrence of each character in the given string:")
print(char_freq)
