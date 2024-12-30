arr=[1,2,3,4]
# arr2=[]
# for i in range(len(arr)-1):
#     arr2.append(arr[i+1])
# arr2.append(arr[0])
# print(arr2)
temp = arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=temp
print(arr)