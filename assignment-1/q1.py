#operations on complex numbers
print("Enter the first complex number:")
real1 = float(input("Real part: "))
imag1 = float(input("Imaginary part: "))
num1 = complex(real1, imag1)

print("\nEnter the second complex number:")
real2 = float(input("Real part: "))
imag2 = float(input("Imaginary part: "))
num2 = complex(real2, imag2)

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2

print("\nSum of the two complex numbers:", sum)
print("Difference of the two complex numbers:", diff)
print("Product of the two complex numbers:", prod)