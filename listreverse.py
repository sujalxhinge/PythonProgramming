revlist = [1,2,3,4,5,6,7,8]

for i in reversed(revlist):
    result = i % 10
    print(result,end=" ")
    i = i // 10

