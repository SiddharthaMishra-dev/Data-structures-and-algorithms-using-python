import sys
arr=[-1,-2,-4,-5,-6,-10]
n=len(arr)
negative=1
for i in range(n):
    if arr[i]>=0:
        negative=0
        break

maxsum= -sys.maxsize
currsum=0
if negative:
    maxsum=max(arr)
else:
    for i in range(n):
        currsum+=arr[i]
        if currsum>maxsum:
            maxsum=currsum
        if currsum<0:
            currsum=0
    
print(maxsum)

# for all negative numbers we have to return maximum element from the array
# Kadane's algorithm works on the concept that if sum of the subarray becomes negative it must be droped as it reduces the overall value of the subarray.