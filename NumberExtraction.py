countd = [1,1,2,2,3,4,5,6,6]
count_dict = {}

for i in range(len(countd)):
    for j in range(i):
        if countd[i] == countd[j]:
            if countd[i] in count_dict:
                count_dict[countd[i]] += 1
            else:
                count_dict[countd[i]] = 2

print(count_dict)
