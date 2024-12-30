arr = [-1,2,3,3,4,5,-1]
k = 4
l = 0
r = k-1
sum = 0
maximum=[]
n=len(arr)
for i in range(l,r+1):
    sum = sum+arr[i]
maximum.append(sum)
while r<n-1:
    sum=sum-arr[l]
    l+=1
    r+=1
    sum = sum+arr[r]
    maximum.append(sum)
print(max(maximum))
    