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
#     st=[]
#     status=True
#     for i in s:
#         if i in '[{(':
#             st.append(i)
#             status= False
#
#         #if i in '[]{}()' and len(s) == 1:
#             #return True
#         elif len(st)!=0 and st[-1] == '{' and i == '}' :
#             st.pop(len(st) - 1)
#             status=True
#
#         elif len(st)!=0 and st[-1] == '[' and i == ']':
#             st.pop(len(st) - 1)
#             status=True
#
#         elif len(st)!=0 and st[-1] == '(' and i == ')':
#             st.pop(len(st) - 1)
#             status=True
#         else:
#             status = False
#     return status
# s="(])"
# print(isValid(s))
    stack = []
    dic = {'(':')','{':'}','[':']'}
    for i in s:
        if i in dic:
            stack.append(i)
        elif len(stack) == 0 or dic[stack.pop()] != i:
            return False
    return len(stack) == 0
s = "({)"
print(isValid(s))


