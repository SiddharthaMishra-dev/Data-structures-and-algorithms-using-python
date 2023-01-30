arr=['hello','world','hell']
minword=min(arr)
print(minword)
prefix=""
for i in arr:
    temp=""
    for j in range(len(minword)):
        if i[j] == minword[j]:
            temp+=minword[j]
    if prefix=="":
        prefix=temp        
    if len(prefix)>len(temp):
        prefix=temp

flag=1
for i in arr:
    if prefix[0] != i[0]:
        flag=0
        break

if flag==1:
    print(prefix)
else:
    print("no common element")

            
    

