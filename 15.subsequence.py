def isSubsequence(s, t):
    count = 0
    lens=len(s)
    lent=len(t)
    j=0
    for i in range(lent):
        if s[j]==t[i]:
            count += 1
            if j == lens-1:
                break

            j+=1

    if count != lens:
        return False
            # if j == lent-1 and t[lent-1] != s[i]:
            #     return False
    else:
        return True

s = "b"
t = "abc"
print(isSubsequence(s,t))