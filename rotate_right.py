arr = [1,2]
length = len(arr)-1
arr2=[]
k = 3
k=k%length
j=0
if len(arr) == 1:
    print("failed")
else:
    for i in range(length,length-k,-1):
        arr2.append(arr[i])
    for i in range(length,k-1,-1):
        arr[i]=arr[i-k]
    for i in range(len(arr2)-1,-1,-1):
        arr[j]=arr2[i]
        j=j+1
print(arr)