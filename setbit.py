N=int(input())
K=3
mask=1<<(K-1)
# print(mask)
newnum=N|mask
print(newnum)