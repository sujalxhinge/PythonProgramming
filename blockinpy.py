# class A:
#     def b(self):
#         print("hello")
#
# obj = A()
# obj.b()


"""Control flow"""
list_list = [1,2,3,4,5,6,7,8,9,10]
for item in range(len(list_list)):
    if list_list[item]  == 2:
        print(list_list[item])
    elif list_list[item]  == 5:
        print(list_list[item])
        break
else:
  print("not found")

