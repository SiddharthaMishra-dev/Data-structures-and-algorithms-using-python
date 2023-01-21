s ="My name is Siddhartha Mishra"
# word=list()
# word=s.split(' ')
# n=len(word)
# for i in range(n):
#     word[i]=word[i][::-1]

# stemp=''
# for i in range(n):
#     stemp=stemp+word[i]+' '
# print(stemp)
words=list()
words=s.split(' ')
n=len(words)
stemp=''
for i in range(n-1,-1,-1):
    stemp=stemp+words[i]+' '

print(stemp)
