heap=[-1,50,30,40,10,5,20,30]
element=60
heap.append(element)
i=len(heap)-1
while(i>1):
    parent=i//2
    if(heap[i]>heap[parent]):
        heap[i],heap[parent]=heap[parent],heap[i]
        i=parent
    else:
        break

print(heap)

