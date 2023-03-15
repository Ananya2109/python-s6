
s1=set()
s2=set()
n1=int(input(f'number of elements in the first set: '))
n2=int(input(f'number of elements in the second set: '))

print(f'enter the elements of the first set: ')
for i in range(n1):
    num=int(input("no:"))
    s1.add(num)

print(f'enter the elements of the second set: ')
for i in range(n2):
    num=int(input("no:"))
    s2.add(num)

print(f's1: {s1}')
print(f's2: {s2}')
print(f's1 union s2 {s1|s2}')
print(f's1 intersection s2 {s1&s2}')
print(f's1 symmetric difference s2 {s1^s2}')