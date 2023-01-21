arr=[1,13,2,6,10,4]
n=len(arr)
res=[]
max=0
for i in range(n-1,-1,-1):
    if arr[i]>max:
        res.append(arr[i])
        max=arr[i]

res.reverse()
print(res)