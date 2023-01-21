arr=[1,8,2,4]
n=4

# First Method



a=[]
result=[0]*n
for i in range(n-1,-1,-1):
    while a and a[-1]<=arr[i]:
        print(a.pop())
    if a:
        result[i]=a[-1]
    a.append(arr[i])
for i in range(n):
    if result[i] == 0:
        result[i]=-1


# Second Method


# for i in range(n):
#     flag=0
#     for j in range(i+1,n):
#         if arr[j] >arr[i]:
#             A.append(arr[j])
#             flag=1
#             break
#     if flag == 0:
#         A.append(-1)
# A.append(-1)


    




print(result)