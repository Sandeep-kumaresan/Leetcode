def BubbleSort(nums):

    while True:
        status = True
        temp=0
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                temp=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
                status=False
        if status == True:
            break
        else:
            continue
    return nums
nums=[2,10,5,3]
print(BubbleSort(nums))