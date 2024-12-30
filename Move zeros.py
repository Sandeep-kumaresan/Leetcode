arr=[0,1]
count = 0
i = 0
for j in range(1,len(arr)):
    if arr[i] == 0 and arr[j]!=0:
        arr[i] = arr[j]
        arr[j] = 0
        count += 1
        
    elif arr[i]==0:
        continue
    if arr[i] == 0 and j == len(arr)-2:
        arr[i]==arr[len(arr)-2]
    else:
        i += 1
print(arr)

