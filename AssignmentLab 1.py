#Question 1
# Arithmatic operators
print("Arithmatic operator")
a = 10
b = 90
sum = a + b
min = b - a
mul = a * b
div = a / b
square = a ** 2
mod = a % b
print(sum)
print(min)
print(mul)
print(div)
print(square)
print(mod)
print("Relational operator")
# relational operators
less = a < b
greater = a > b
greater_equal = a >= b
less_equal = a <= b
equal = a == b
not_equal = a != b
print(less)
print(greater)
print(greater_equal)
print(less_equal)
print(equal)
print(not_equal)
print("Logical operator")
# Logical operators
andoperator = a & b
oroperator = a | b
xoroperator = a ^ b
print(andoperator)
print(oroperator)
print(xoroperator)
print("Bitwise operator")
# Bitwise operator
bitwiseoperator = a ^ b
bitwiseandoperator = a & b
bitwiseoroperator = a | b
bitwisexoroperator = a ^ b
print(andoperator)
print(oroperator)
print(xoroperator)
print("Assignment operator")
# Assignment operator
assignment = 10000
print(assignment)


#Question 4
Set_1 = {11,20,30,49,59,69,79,89,99,100}
# print(Set_1.remove(99))
list_1 = [1,2,3,4,5]
print("after update")
Set_1.update(list_1)
print(Set_1)

Set_1.add(101)
print("after adding 100")
print(Set_1)

from countduplicate import duplicate

Question 5

Dict_1 = {"name":"sujal","age":25,"city":"shanghai"}
for key,value in Dict_1.items():
    print(key," : ",value)

Question 2


print(type(20))
print(type(20.00))
print(type("sujal"))
print(type(True))

#Question 3
Str_1 = "Harshal"
Str_2 = "Sarthak"
print(Str_1[:2])
print(Str_1[:])
print("Concatanation of string")
print(Str_1 + Str_2)

duplicate = []
for i in Str_1:
    count = Str_1.count(i)
    if Str_1.count(i):
        print(f"{i} : {count}")
        duplicate.append(i)

Question 6
list_1 = [1,2,3,4,5]
print("after adding element in list")
list_1.append(6)
print(list_1)
print("after inserting element in list")
list_1.insert(1,7)
print(list_1)
print("after removing element from list")
list_1.remove(7)
print(list_1)
print("after pop element")
list_1.pop()
print(list_1)
print("after sorting element in list")
list_1.sort()
print(list_1)
print("after reverse element in list")
list_1.reverse()
print(list_1)

Question 7
number = 50
if number < 0 :
    print("Number is negative")
elif number > 0 :
    print("Number is positive")
elif number == 0 :
    print("Number is zero")

Question 8
even = []
for i in range(1,50):
    if i % 2 == 0:
        even.append(i)
print(even)

Question 9
number = 111
sum_digits = 0

n = number
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(sum_digits)

Question 10
Str_1 = "Sujal"
list_1 = ['a','e','i','o','u']
for vowel in Str_1:
    if vowel in list_1:
        print(vowel,end= "")


