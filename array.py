# from itertools import count
#
# alist = [2200,2350,2600,2130,2190]
# alist.insert(5,1980)
# exp = alist[0]+alist[1]+alist[2]
#
# print(f"you have spent $ {exp} in a Quarter")

MY_Dict = [
           {"name":"sujal","age":18},
           {"name": "sarthak", "age": 19},
           {"name":"om","age":16},
           {"name":"mohit","age":26},
           {"name":"abhjit","age":55}
          ]
for item in MY_Dict:
    if item["age"] < 18:
        continue
    print(item["name"], item["age"])

