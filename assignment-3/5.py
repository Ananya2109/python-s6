l=[]
for i in range(10):
    num=int(input("no: "))
    l.append(num)
t=tuple(l)
print(f'tuple is: {t}\nsum: {sum(t)}\naverage: {sum(t)/10}')
print(f'largest no: {max(t)}\nsmallest no: {min(t)}')