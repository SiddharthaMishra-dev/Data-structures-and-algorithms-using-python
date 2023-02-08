
arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
x=5
left=-1
right=-1
flag=0
for i in range(len(arr)):
    if flag ==0  and arr[i] ==x:
        flag=1
        left=i
    
    if flag ==1 and arr[i]==x:
        right=i

res=[left,right]
print(res)