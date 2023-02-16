arr=[4,5,1,2,3]
d=2
n=len(arr)
num=2
low=0
high=n-1
index=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==num:
        index=mid
        break

    #Left part is sorted

    if arr[low]<arr[mid]:
        if num>=arr[low] and num<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    
    #right part is sorted

    else:
        if num>arr[mid] and num<=arr[high]:
            low=mid+1
        else:
            high=mid-1




print(index)
