"""Leetcode-283
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

nums=[45192,27382,-659,-52359,-99225,-75991,0,-15155,0,59818,0,-30645,-17025,81209,887,64648]
i=0
for j in range(1,len(nums)):
    if nums[i]>0:
        i+=1
    elif nums[j]>0 and nums[i] == 0:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        i+=1
        #iter
print(nums)