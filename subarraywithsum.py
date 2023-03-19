arr=[10,5,20,-15,-10,11]
sum=5
maparr=[0]*len(arr)
currsum=0
start=0
end=-1
for i in range(len(arr)):
    currsum=currsum+arr[i]
    if currsum==sum:
        end=i
        break
    if maparr.index(currsum-sum)>=0:
        start=maparr.index(currsum-sum)+1
        end=i
        break
    maparr[i]=currsum

print(start,end)
