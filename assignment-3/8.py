str=input("Enter the string: ")
words=str.split(" ")
sum=0
avg=0.0
count=0
for w in words:
    l=len(w)
    sum+=len(w)
    count+=1
    print(f'length of {w}: {l}')
avg=sum/count
print(f'average: {avg}')
