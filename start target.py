class starttarget:
    def elem(self,arr,target):
        ind=[]
        for i in range(len(arr)):
            if arr[i] == target:
                ind.append(i)
        return [ind[0],ind[len(ind)-1]]

    def elem2(self,arr,target):
        for i in range(len(arr)):
            if arr[i] == target:
                start = i
                while i+1 < len(arr) and arr[i+1] == target:
                    i+=1
                return [start,i]
        return [-1,-1]

obj = starttarget()
arr = [2,3,4,4,4,5,6]
target = 4
# print(obj.elem(arr,target))
print(obj.elem2(arr,target))