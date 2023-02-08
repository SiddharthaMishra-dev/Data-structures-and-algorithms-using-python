arr=[1,2,3]
res=0

if(arr[-1]<9):arr[-1]=arr[-1]+1;print(arr) 

for i in arr:
    res=res*10+i
res+=1

print(list(str(res)))
