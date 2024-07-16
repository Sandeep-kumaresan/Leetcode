"""remove duplicates in same array until unique elements leave remaining,
return no.of unique elements"""
def removeDuplicates(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            nums[i+1]=nums[j]
            i+=1
    return i+1
             
nums=[1,2,3,3,4]
print(removeDuplicates(nums))