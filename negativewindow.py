A=[12, -1, -7, 8, -15, 30, 16, 28]
k=3
n=len(A)
result=[]
loop=n-k+1
for i in range(loop):
    temp=A[i:i+k]
    # print(temp)
    flag=0
    number=0
    for j in range(len(temp)):
        if flag==0 and temp[j]<0:
            flag=1
            number=temp[j]
    result.append(number)

# print(result)

A.reverse()
print(A)