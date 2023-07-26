# This program checks if given number is prime or not
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5), +1):
        if num % i == 0:
            return False
    else:
        return True
num = int(input("Enter your number: "))
print(prime(num))