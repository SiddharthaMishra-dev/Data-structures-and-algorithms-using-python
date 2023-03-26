# k largest element
import heapq

arr=[10,2,9,22,90,1,48]
k=3

heapq.heapify(arr)

print(heapq.nlargest(k,arr))
