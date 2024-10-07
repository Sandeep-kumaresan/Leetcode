a = "aab"
b = a.split(" ")
if len(b) == 1:
    print(0)
else :
    for i in range(1):
        if b[i] in b[i+1]:
            print(1)
        else:
            print(0)