import math
n=int(input())
temp=int(math.sqrt(n))
boolarray=[True]*(n+1)
boolarray[0]=False
boolarray[1]=False
for i in range(2,temp+1,1):
    j=2*i
    while j<=n:
        boolarray[j]=False
        j+=i

for i in range(n):
    print( i , boolarray[i])