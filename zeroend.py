n = int(input())
j=0
lis = [0 for i in range(n)]
for i in range(n):
    a = int(input())
    if a != 0:
        lis[j] = a
        j += 1
for i in lis:
    print(i)