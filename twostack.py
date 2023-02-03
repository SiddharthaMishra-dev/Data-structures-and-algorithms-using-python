arr=[-1]*100
def push1(arr,x):
    arr.insert(0,x)
def push2(arr,x):
    arr.insert(len(arr),x)
def pop1(arr):
    if len(arr):
        arr.pop(0)
    else:
        print("no data in list")
def pop2(arr):
    if len(arr):
        arr.pop(len(arr)-1)
    else:
        print("no data in the list")

