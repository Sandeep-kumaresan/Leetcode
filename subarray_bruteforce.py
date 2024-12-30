arr = [2,5,1,7,10]
n=len(arr)
k=14
maxel=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum = sum+arr[j]
        if sum<=k:
            maxel=max(maxel,j-i+1)
print(maxel)