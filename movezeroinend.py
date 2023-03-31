arr=[0,1,0,3,12]
temp=list()
for i in range(len(arr)):
    if(arr[i]!=0):
        temp.append(arr[i])

l=len(arr)-len(temp)
for j in range(l):
    temp.append(0)

arr=temp
print(arr)