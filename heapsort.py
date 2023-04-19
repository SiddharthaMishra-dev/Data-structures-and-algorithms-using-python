import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_list=list()
    while(arr):
        element=heapq.heappop(arr)
        sorted_list.append(element)
    return sorted_list


arr=[10,2,11,29,9,33,8,0,90]
print(heap_sort(arr))
