s1="siddhartha"
s2='siddhantha'
temp=[]
for i in s1:
    if i not in temp:
        temp.append(i)

print(temp)