import math
# A=10
# B=20
# C=A^B
# count=0
# while C!= 0:
#     if C&1 ==1:
#         count=count+1
#     C=C>>1

# print(count)
N=42
nbit=int(math.log(N,2)+1)
mask=0<<nbit
temp = N^mask
print(temp)