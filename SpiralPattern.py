n=int(input("Enter a number: "))
l=[0]*n
val=[0]*n

for i in range(n):
    for j in range(n):
        val[j]=int(input())
    l[i]=val
    val=[0]*n

temp=0
rs,cs=0,0
re,ce=n-1,n-1

while n:
    if temp==0:
        i=rs
        for j in range(re+1):
            print(l[i][j],end=" ")

        rs+=1
        temp+=1

    elif temp==1:
        j=ce
        for i in range(rs,re+1):
            print(l[i][j],end=" ")
        ce-=1
        temp+=1

    elif temp==2:
        i=re
        for j in range(ce,cs-1,-1):
            print(l[i][j],end=" ")
        re-=1
        temp+=1

    else:
        j=cs
        for i in range(re,rs,-1):
            print(l[i][j],end=" ")
        cs+=1
        temp=0

    if rs>re and cs>ce:
        break






