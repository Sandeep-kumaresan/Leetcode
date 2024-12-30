nums=[3,0,1]
n=len(nums)+1
# count=0
# for i in range(len(nums)):
#     if i not in nums:
#         count+=1
#         print(i)
# if count ==0:
#     print(max(nums)+1)


#  n = len(nums)
#         v = [-1] * (n + 1)
#         for num in nums:
#             v[num] = num
#         for i in range(len(v)):
#             if v[i] == -1:
#                 return i
#         return 0

hash = [0]*n

for i in range(len(nums)):
    if nums[i]:
        hash[nums[i]]+=1
for i in range(len(hash)):
    if hash[i] == 0:
        print(i)