# Moore's voting Algorithm for major element in an Array

arr=[1,2,3,4,5]
major=arr[0]
count=1
n=len(arr)
for i in range(1,n):
    if major==arr[i]:
        count+=1
    else:
        count-=1
    if count ==0:
        major=arr[i]

c=0
for i in range(n):
    if major==arr[i]:
        c+=1

if c>n//2:
    print(major)
else:
    print("No answer")


# This algorithm works on the concept element priority in the array.
# if next index number is same as preceeding number then importance of the element increases otherwise decreases.