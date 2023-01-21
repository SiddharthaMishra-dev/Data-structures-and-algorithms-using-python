def power(a,b):
    if b==0:
        return 1
    return power(a,b-1)*a

def gcdnumber(a,b):
    if b>a:
        return gcdnumber(b,a)
    if b==0:
        return a
    else:
        return gcdnumber(b,a%b)

arr=[[1,2,3],[4,5,6],[7,8,9]]
n=3
m=3
def findWays(n,m):
    if n==1 or m==1:
        return 1
    return findWays(n-1,m)+findWays(n,m-1)

# print(power(10,5))
# print(gcdnumber(4,8))
print(findWays(3,3))