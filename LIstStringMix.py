import string

ListString = [3,4,"sujal","harshada","atharv",1,2]
names = []
nums =[]

for i in ListString:
    if type(i) == str:
        names.append(i)
    elif type(i)== int:
        nums.append(i)

print(names)
print(nums)

