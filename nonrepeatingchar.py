s="siddhartha"
temp=dict()
for key in s:
    if key in temp:
        temp[key]+=1
    else:
        temp[key]=1
for key in s:
    if temp[key]==1:
        print(key)
        
    
