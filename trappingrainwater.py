arr=[3,1,2,4,0,1,3,2]
n=len(arr)
left=[]
right=[0]*n
left.append(arr[0])
for i in range(1,n):
    left.append(max(arr[i],left[i-1]))

print(left)
right[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    right[i]=max(right[i+1],arr[i])
    

total=0
for i in range(0,n):
    total=total+(min(left[i],right[i])-arr[i])
print(total)