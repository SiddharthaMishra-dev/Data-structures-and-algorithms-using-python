arr=[1,2,5,7,8,10,2,2,5]
n=len(arr)
minsofar=arr[0]
maxprofit=0
for i in range(1,n):
    if minsofar>arr[i]:
        minsofar=arr[i]
    if arr[i]-minsofar >maxprofit:
        maxprofit=arr[i]-minsofar

print(maxprofit)