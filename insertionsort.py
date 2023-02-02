arr=[10,4,5,11,9,8,6]
n=len(arr)
for i in range(n):
    temp=arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp

print(arr)
