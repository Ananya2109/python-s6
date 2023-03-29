L = [(16, 'ananya'), (3, 'anu'), (2, 'bob')]

sorted_by_rno = sorted(L, key=lambda x: x[0])
print(sorted_by_rno)

sorted_by_name = sorted(L, key=lambda x: x[1])
print(sorted_by_name)
