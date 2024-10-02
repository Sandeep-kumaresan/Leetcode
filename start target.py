class starttarget:
    def elem(self,arr,target):
        ind=[]
        for i in range(len(arr)):
            if arr[i] == target:
                ind.append(i)
        return ind[0],ind[len(ind)-1]

obj = starttarget()
arr = [2,3,4,4,4,5,6]
print(obj.elem(arr,target=4))
