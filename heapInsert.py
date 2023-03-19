heap=[-1,50,30,40,10,5,20,30,60]
value=45
heap.append(value)
i=len(heap)-1
while i>1:
    parent=i//2
    if heap[parent]<heap[i]:
        heap[parent],heap[i]=heap[i],heap[parent]
        i=parent
    else:
        break

print(heap)

