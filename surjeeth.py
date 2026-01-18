n = int(input("enter n:"))
for x in range(n,0,-1):
    for y in range(1,x+1):
        print("*",end="")
    for z in range(1,2*(n-x)+1):
        print(" ",end="")
    for m in range(1,x+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for k in range(1,2*(n-i)+1):
        print(" ",end="")
    for l in range(1,i+1):
        print("*",end="")
    print()