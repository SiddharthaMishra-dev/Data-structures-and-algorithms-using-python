arr =[4,5,3,222,34,11,1]
def bubbleSort(n,arr):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


n=len(arr)
print("Array before Sort\n")
print(arr)
bubbleSort(n,arr)
print("\nsorted array\n")
print(arr)