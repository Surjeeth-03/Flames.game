a=list(map(int,input().split()))
target=int(input())
left=0
right=len(a)-1
x=-1
while left<=right:
    mid=(left+right)//2
    if(target==a[mid]):
        x=mid
        break
    elif(target<a[mid]):
        right=mid-1
    elif(target>a[mid]):
        left=mid+1
if(x==-1):
    print("-1")
else:
    print(x)