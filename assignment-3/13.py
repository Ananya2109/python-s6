l=[]
n=int(input("Enter the elements of the list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list l is: {l}')
s=set(l)

#find highest frequency
max=0
for num in s:
    if l.count(num)>=max:
     max=l.count(num)

#print numbers with highest frequency
largest=[]
for num in s:
   if l.count(num)==max:
      largest.append(num)

print(f'No:(s) with largest occurrence: {largest} with frequency {max}')