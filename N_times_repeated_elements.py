n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
e=[]
for i in a:
    if a.count(i)==k:
        e.append(i)
        c+=1
d=set(e)
for j in d:
    print(j,end=' ')
if c==0:
    print('-1')
    