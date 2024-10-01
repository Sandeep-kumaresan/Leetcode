def longestCommonPrefix(strs):
    minlength=float('inf')
    for s in strs:
        if len(s) < minlength:
            minlength = len(s)
    i = 0

    while i < minlength:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1
    # print(len(strs))
    # if len(strs)==1:
    #     return strs[0]

strs = ["ab","ac","ab"]
print(longestCommonPrefix(strs))