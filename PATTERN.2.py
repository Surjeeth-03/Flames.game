n=input()
a=list(n)
b=a[::-1]
an=input()
aa=list(an)
bb=aa[::-1]
for x in range(len(a)-1,-1,-1):
    for y in range(0,x+1):
        print(a[y],end="")
    for z in range(0,(2*(len(n)-x)-1)):
        print(" ",end="")
    for p in range(0,x+1):
        print(aa[p],end="")
    print()

for i in range(1,len(a)):
    for j in range(0,i+1):
        print(aa[j],end="")
    for k in range(0,(2*(len(n)-i)-1)):
        print(" ",end="")
    for l in range(0,i+1):
        print(a[l],end="")
    print()