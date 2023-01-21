arr=[12,5,10,2,4,7,20,21]
n=len(arr)
left=0
right=0
sum=21
count=0
for i in range(n):
    for j in range(i,n):
        count+=arr[j]
        if count == sum:
            left=i
            right=j
    

print(left,right)
        
    

