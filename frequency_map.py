nums=[1,2,3,4,5,1,1,2,4,5]
"""
freq_map={}
for i in range (0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)"""
hash_map = {}
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
print(hash_map)
