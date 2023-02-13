arr=[1,2,3,4,5]
# k is number of times array will be rotated
k=2
temp=[0]*len(arr)
for i in range(len(arr)):
    temp[(i+k)%len(arr)]=arr[i]

print(temp)

