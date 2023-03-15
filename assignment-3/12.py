l=[]
n=int(input("Enter the elements of the list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list l is: {l}')
s=set(l)
print(f'After removing duplicates in l: {list(s)}')