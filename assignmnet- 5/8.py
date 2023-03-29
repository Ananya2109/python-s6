def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [11, 12, 65, 1, 86]
result = find_largest(numbers)
print(result) 
