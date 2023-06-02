n=int(input())
for i in range(0,n):
    a=int(input())
    e=list(map(int,input().split()))
    d=sorted(e)
    if d==e:
        print('0')
    else:
        print(max(e)-min(e))