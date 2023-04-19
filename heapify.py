
def heapify(arr,n,i):
    largest=i
    l=i*2 +1
    r=i*2 +2
    if(l<n and arr[largest]<arr[l]):
        largest=l
    if(r<n and arr[largest]<arr[r]):
        largest=r
    if(largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
def buildHeap(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

def heapSort(arr,n):
    buildHeap(arr,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

arr=[10,22,2,90,3,44]
n=len(arr)
heapSort(arr,n)
print(arr)



