#to print all prime number less than 100
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for num in range(2, 100):
    if is_prime(num):
        print(num, end=" ")
