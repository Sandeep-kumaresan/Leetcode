n = int(input())
arr = map(int, input().split())
new_arr = list(set(arr))
print(new_arr)
new_arr.sort()
max=new_arr[-2]
print(max)