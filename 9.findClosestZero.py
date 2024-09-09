#want to complete
# def findClosestNumber(nums):
#     min = 999999
#     for i in nums:
#         if abs(i) > 0 and abs(i) < abs(min) :
#             min = i
#         if abs(i) == 0:
#             min = 0
#     return min
def findClosestNumber(self, nums):
    CloseNum = nums[0]

    for i in nums:
        if abs(i) < abs(CloseNum):
            CloseNum = i

    if CloseNum < 0 and abs(CloseNum) in nums:
        return abs(CloseNum)
    return CloseNum
nums = [-4, -2, 1, 4, 8]
print(findClosestNumber(nums))
