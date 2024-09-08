#completed
def removeElement(nums, val):
    # count=0
    # temp=0
    # j=len(nums)-1
    # for i in range(len(nums)):
    #     if i == j:
    #         break
    #         nums = nums
    #     else:
    #         if nums[j] == val:
    #             j-=1
    #         if nums[i] == val:
    #             temp = nums[i]
    #             nums[i] = nums[j]
    #             nums[j] = temp
    #             count+=1
    #             j-=1
    #         else:
    #             continue
    # k = (len(nums)-1)-(count)
    # return k
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index
nums= [0,1,2,2,3,0,4,2]
print(removeElement(nums,val=2))