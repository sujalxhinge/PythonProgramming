# Dict ={
#         "s1": {"name":"Sujal","age":22},
#         "s2": {"name":"Sarthak","age":19},
#       }
# for i,obj in Dict.items():
#     print(i)
#     for k,v in obj.items():
#         print(k, ":" , v)

# import array as arr
#
# # Create an integer array
# numbers = arr.array('i', [10, 25, 3, 45, 7, 89, 15])
#
# # Initialize max and min with the first element
# max_num = numbers[0]
# min_num = numbers[0]
#
# # Loop through array elements
# for num in numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
#
# # Print results
# print("Array elements:", numbers.tolist())
# print("Maximum number:", max_num)
# print("Minimum number:", min_num)

Dict ={
        "s1": {"name":"Sujal","age":22},
        "s2": {"name":"Sarthak","age":19},
      }

for i,obj in Dict.items():
    print(i)
    for j in obj:
        print(j+":",obj[j])


