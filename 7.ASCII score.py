s="hello"
res=0
for i in range(len(s)-1):
    res+=abs(ord(s[i])-ord(s[i+1]))
print(res)