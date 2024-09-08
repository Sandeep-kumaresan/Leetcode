def Selectionsort(nums):
    for ind in range(len(nums)-1):
        min=ind
        for i in range(ind+1,len(nums)):
            if nums[i]<nums[min]:
                min=i
        nums[min],nums[ind]=nums[ind],nums[min]
    return nums
nums=[8,5,1,3,2]
print(Selectionsort(nums))