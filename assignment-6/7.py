import math 
n = int(input("enter n: "))
x = int(input("enter x: "))
sum = 0
print("series: ",end=" ")
for i in range(0,n+1,2):
    temp =1
    if(i==1):
        pass
    elif i%4 ==1:
        print("+", end=" ")
    else:
        temp*= -1
        print("-",end =" ")
    if i==-1:
        print("x", end=" ")
    else:
        print("x^{}/{}!".format(i,i),end=" ")
    temp*=(x**i)/math.factorial(i)
    sum+= temp
    
print()
print("sum: {}\n".format(sum))



