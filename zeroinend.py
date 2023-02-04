arr=[1,20,0,5,9,10]
n=len(arr)
temp=[0]*n
index=0
for i in arr:
    if i!=0:
        temp[index]=i
        index+=1

arr[::]=temp
print(arr)

