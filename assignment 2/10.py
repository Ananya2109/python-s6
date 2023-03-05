#10.   Input a number and print it in words(i/p: 345 o/p: Three Four Five)
n = input("Enter a number: ")
words = []
for digit in n:
    if digit == "0":
        words.append("Zero")
    elif digit == "1":
        words.append("One")
    elif digit == "2":
        words.append("Two")
    elif digit == "3":
        words.append("Three")
    elif digit == "4":
        words.append("Four")
    elif digit == "5":
        words.append("Five")
    elif digit == "6":
        words.append("Six")
    elif digit == "7":
        words.append("Seven")
    elif digit == "8":
        words.append("Eight")
    elif digit == "9":
        words.append("Nine")
print(" ".join(words))
