stack=[41,3,32,2,11]

def sortinsert(stack,n):
    if not stack or stack[-1]<n:
        stack.append(n)
        return
    temp=stack[-1]
    stack.pop()
    sortinsert(stack,n)
    stack.append(temp)

def stacksort(stack):
    if len(stack)==0:
        return
    n=stack[-1]
    stack.pop()
    stacksort(stack)
    sortinsert(stack,n)



stacksort(stack)
print(stack)
    

    

