def mergeAlternately(word1, word2):
    out = ""
    l=max(len(word1),len(word2))
    for i in range(l):
        if (len(word1)-1) < i:
            out+=word2[i]
        elif (len(word2)-1) < i:
            out += word1[i]
        else:
            out+=word1[i]
            out+=word2[i]
    return out
w1="ab"
w2="pqrs"
print(mergeAlternately(w1,w2))