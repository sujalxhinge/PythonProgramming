evenoddsquare = [1,2,3,4,5,6,7,8,9]
evesq = []

for i in range(1,len(evenoddsquare)):
    if evenoddsquare[i] % 2 == 0 :
        evesq.append(evenoddsquare[i] ** 2)
print(evesq)

