def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # count=0
    # count2=0
    # count3=0
    # for i in s:
    #     if i == '[':
    #         count += 1
    #     elif i == ']':
    #         count -= 1
    #     elif i == '{':
    #         count2 += 1
    #     elif i == '}':
    #         count2 -= 1
    #     elif i == '(':
    #         count3 += 1
    #     elif i == ')':
    #         count3 -= 1
    # if count == 0 and count2 == 0 and count3 == 0:
    #     return True
    # else:
    #     return False
    for i in s:
        if s in '[{(':


