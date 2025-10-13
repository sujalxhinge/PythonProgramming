list = []
for i in range(10):
    n = int(input("Enter Numbers :"))
    list.append(n)
even = []
odd = []
for i in list:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)
print("even numbers -->  ",even)
print("odd numbers  -->  ",odd)

max_item = max(list)
print("max element is list",max_item)

min_item = min(list)
print("minimum item in list",min_item)

sum_item = sum(list)
print("total sum of",sum_item)

average = sum(list)/len(list)
print("total average",average)












