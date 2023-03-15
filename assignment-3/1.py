stud=[]
print(f'stud initially: {stud}')
rollno=[64]
#adding elements using: concatenation,append(),extend(),insert()
stud=stud+rollno
stud.append("Sreya")
details=["Kochi","682021","9712342102"]
stud.extend(details)
stud.insert(0,"MDL20CS115")
print("KTUid: ",stud[0]," name: ",stud[2]) 
print(f'number of characters in name: {len(stud[2])}')
print(f'last 4 digits of phone number: {stud[5][-5:]}')
print(f'reversed list is:{stud[::-1]}')
print(f'index of name: {stud.index("Sreya")}')