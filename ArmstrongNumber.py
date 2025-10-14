armstrongNum = 153
number = armstrongNum
n = len(str(armstrongNum))
# Number of digits in the number

sum = 0                            # To store sum of each digit raised to n
temp = number                      # Copy for calculation

while temp > 0:
    digit = temp % 10              # Get the last digit
    sum += digit ** n              # Add digit raised to power n
    temp = temp // 10              # Remove last digit

if sum == armstrongNum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")
