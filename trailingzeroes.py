n=int(input())
res=0
for i in range(5,n,*5):
    res+=n/i

print(res)
