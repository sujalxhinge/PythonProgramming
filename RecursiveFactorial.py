def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

n = int(input("Enter the number: "))
print(recursive_factorial(n))
