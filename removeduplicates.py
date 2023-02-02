s="aabbbcd"
temp=""
for i in s:
    if i not in temp:
        temp+=i

print(temp)