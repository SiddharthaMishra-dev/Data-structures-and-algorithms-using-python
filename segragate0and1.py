arr=[0,0,1,1,1,0,0]
n=len(arr)
arr0=[]
arr1=[]
for i in range(n):
    if arr[i] ==1:
        arr1.append(arr[i])
    else:
        arr0.append(arr[i])

arr=arr0+arr1
print(arr)