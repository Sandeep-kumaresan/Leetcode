n=int(input("enter a number:"))
count=0
j=1
for i in range(n+1):
    sum=0
    for j in range(i,n+1):
        if i == j:
            continue
        sum+=j
        if sum==n:
            count+=1
            break
print(count)