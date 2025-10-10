
# for i in range(1,n+1):
#     factorial = factorial * i
#     print("Factorial of",n,"is",factorial)
#
def re(n):
    if n < 1:
        return 1
    else:
        return n * re(n-1)


print(re(5))

