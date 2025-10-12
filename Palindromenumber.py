n = 121121
nums = n
result = 0

while nums > 0:
    last_digit = nums % 10
    result = (result * 10) + last_digit
    nums = nums // 10

if result != n:
    print("Number is not palindrome")
else:
    print("Number is palindrome")
