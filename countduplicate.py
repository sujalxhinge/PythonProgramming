# countd = [1,1,2,2,3,4,5,6,6]
# count = []
# for i in range (len(countd)):
#     for j in range (i):
#         if countd[i] == countd[j]:
#             count.append(countd[i])
# print(count)

countd = [1,1,2,2,3,4,5,6,6]
duplicate = []
for i in range (len(countd)):
    count = countd.count(i)
    if count > 1 and i not in duplicate:
        print(f"{i} : {count}")
        duplicate.append(i)