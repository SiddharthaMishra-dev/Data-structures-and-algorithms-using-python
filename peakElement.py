arr =[1,4,2,3,5,6,9,0]
n= len(arr)
peakelement=0
if n==1:
    peakelement=arr[1]
else:
    for i in range(n):
        if i==0:
            if arr[i]>=arr[i+1]:
                peakelement=arr[i]
        elif i == n-1:
            if arr[i]>=arr[i-1]:
                peakelement=arr[i]
        
        else:
            if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
                peakelement=arr[i]
    
print(peakelement)