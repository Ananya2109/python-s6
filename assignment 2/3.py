#.1
#1 2
# 1 2 3
#1 2 3 4
#The pyramid is given for n=4 do this for any n


n = int(input("Enter the value of n: "))


for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

