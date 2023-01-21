a=[7,2,1,9,10]
n=len(a)
sum=0
cur=0
position=-1
for i in range(n):
    sum+=a[i]

for i in range(0,n):
    sum-=a[i]
    if sum == cur:
        position= i+1
    cur=cur+a[i]
print(position)
     