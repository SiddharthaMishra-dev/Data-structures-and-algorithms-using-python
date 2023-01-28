arr=[1,2,10,5,-1,6,-2,0,11,-9]
n=len(arr)
temp=list()
neg=list()
for i in range(n):
    if arr[i]>=0:
        temp.append(arr[i])
    elif arr[i]<0:
        neg.append(arr[i])
    
arr=temp+neg
print(arr)