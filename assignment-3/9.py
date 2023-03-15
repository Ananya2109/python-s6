import math

# Read input numbers
numbers = input("Enter a list of numbers, separated by spaces: ")
numbers = numbers.split()
numbers = [float(num) for num in numbers]

# Calculate mean
mean = sum(numbers) / len(numbers)

# Calculate median
numbers.sort()
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
else:
    median = numbers[len(numbers)//2]

# Calculate standard deviation
std_dev = math.sqrt(sum([(num - mean)**2 for num in numbers]) / len(numbers))

# Print results
print("Mean =", mean)
print("Median =", median)
print("Standard deviation =", std_dev)
