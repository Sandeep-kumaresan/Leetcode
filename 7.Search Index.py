def searchInsert(nums, target):
    start=0
    end=len(nums)-1
    mid=0
    while start<=end:
        mid=(start+end)//2
        if target<nums[mid]:
            end=mid-1
        elif target>nums[mid]:
            start=mid+1
        else:
            return mid
    return start
nums=[1,3,5,6,7]
target=4
print(searchInsert(nums,target))