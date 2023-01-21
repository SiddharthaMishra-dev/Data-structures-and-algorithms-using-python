def powerset(S,i,curr):
    if i == len(S):
        print(curr)
        return
    powerset(S,i+1,curr)
    powerset(S,i+1,curr+S[i])

i=0
curr=''
S=input()
powerset(S,i,curr)
