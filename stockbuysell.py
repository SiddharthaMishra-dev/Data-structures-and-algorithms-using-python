arr=[100 ,180, 260, 310, 40, 535, 695]
n=len(arr)
aux=[0]*n
aux[n-1]=arr[n-1]
result=[[]]
for i in range(n-2,-1,-1):
    aux[i]=max(aux[i+1],arr[i])
print(aux)

max=0
for i in range(n):
    if (aux[i]-arr[i])>max:
        result[0]=[arr[i],aux[i]]
        max=aux[i]-arr[i]
    elif (aux[i]-arr[i])==max:
        result.append([arr[i],aux[i]])

print(result)
