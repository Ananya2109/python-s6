l=[]
n=int(input("Enter the number of elements in the list: "))
for x in range(n):
    num=int(input("no: "))
    l.append(num)
print(l)

flag=0
l1=list()
l2=list()
for i in l:
    for j in range(2,i//2):
        if i%j==0 and i!=1:
            l1.append(i)
            flag=1
    if flag==0 and i!=1:
        l2.append(i)
print(f'list of prime numbers: {l2}\nlist of composite numbers: {l1}')