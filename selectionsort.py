arr=[1,4,9,2,6]
n=len(arr)
for i in range(n-1):
    tempindex=arr.index(min(arr[i:n]))
    arr[tempindex],arr[i]=arr[i],arr[tempindex]

print(arr)
