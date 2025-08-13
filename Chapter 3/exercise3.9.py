num = int(input("Enter a five-digit integer: "))

for i in range(4, -1, -1):
    divisor = 10 ** i
    digit = num // divisor
    print(digit, end=' ')
    num = num % divisor
