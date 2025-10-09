from __future__ import print_function
"""
for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("Square of", i,"is", i**2)

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i*j,end=" ")
    print()"""

"""rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
    *
   ***
  *****
 *******
    
"""

"""rows = 5
for i in range(rows ,0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
 *******
  *****
   ***
    *"""

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
