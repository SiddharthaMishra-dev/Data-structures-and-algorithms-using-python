arr=[1,3,2,4]
n=len(arr)
stack=[]
result=[0]*n
for i in range(n-1,-1,-1):
    while stack and stack[-1]<=arr[i]:
        stack.pop()
    if stack:
        result[i]=stack[-1]
    stack.append(arr[i])

for i in range(n):
    if result[i]==0:
        result[i]=-1

print(result)