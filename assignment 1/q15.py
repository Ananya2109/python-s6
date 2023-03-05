#to print fibonacci series
n = int(input("Enter the number of terms in the series: "))
a, b = 0, 1
print(a)
print(b)
i = 2
while i < n:
    c = a + b
    a, b = b, c
    print(c)
    i += 1
