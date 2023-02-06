def findFloor(self,A,N,X):
        #Your code here
        l=[]
        for i in range(N):
            if A[i]<=X:
                l.append(A[i])
        
        if len(l)==0:
            return -1
        else:
            return A.index(l[-1])