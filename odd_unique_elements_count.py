n=int(input())
a=list(map(int,input().split()))
c=0
d=set(a)
for i in d:
    if i%2!=0 and i!=0:
        c+=1
print(c)