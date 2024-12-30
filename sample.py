def func(arr):
    for i in range(len(arr)-1):
        if (arr[i] % 2 == arr[i+1] % 2):
            return False
    return True

arr = [1,2,4,5]
print(func(arr))