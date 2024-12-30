num=int(input("Enter numerator"))
den=int(input("Enter denominator"))
#def fract(num,den):
den1=str(den)
count=len(den1)
#for i in range(len(den1)):
    #for j in range(len(den1)):
        #if i==j:
            #break
        #if den1[i]==den1[j]:
            #count+=1
res=num/den
res1=str(res)
if res1[2]=="0":
    count+=1
if res1[len(res1)-1]>="5":
    res2=round(res,count)+1
#while den>0:
    #deno=den%10
    #den=den//10
    #if deno==den:
        #count+=1
#return res
res2=round(res,count)
result=str(res2)
if len(res1)>3:
    print(result[0],result[1],"(",result[2:],")")
else:
    print(res2)
print(type(result))