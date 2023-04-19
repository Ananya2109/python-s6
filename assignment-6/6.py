binstr = input("enter a binary number: ")

integerpart = binstr.split(".")[0]
fractionalpart = binstr.split(".")[1]
decstr = 0
for idx,c in enumerate(integerpart):
    decstr+=float(c)*2**(len(integerpart)-idx-1)
for idx,c in enumerate(fractionalpart):
    decstr+=float(c)*2**(-idx-1)

print(decstr)

