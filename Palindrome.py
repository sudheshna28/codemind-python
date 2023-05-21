n=int(input())
sum=0
q=n
while n!=0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if sum==q:
    print('True')
else:
    print('False')