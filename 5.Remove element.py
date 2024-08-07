#not completed
def removeElement(nums, val):
    dums = []
    for i in range(len(nums)):
        if i+1<len(nums):
            if nums[i] == val and nums[i]+1!=val:
                temp=nums[i]

            elif nums[i]== val and nums[i]+1==val:
                nums.pop(i)
                dums.append(i)
                nums.pop(i+1)
                dums.append(i+1)
    nums += dums
    return nums
nums=[1,2,2,3]
val=2
print(removeElement(nums,val))