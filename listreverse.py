revlist = [1,2,3,4,5,6,7,8]
for x in reversed(revlist):
  rev = x % 10
  print(rev,end= " ")
  x = x // 10

