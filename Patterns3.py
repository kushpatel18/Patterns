def Pattern64(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j>0 and i+j<=(n-1)-1 and i>0 )  or(i==n//4 and j==3*n//4 ) or(i==n//2  and j==n//2) or(i==3*n//4 and j==n//4) and not (i==n-1 and i+j==n-1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern65(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j<=n-1 and i+j>=(n-1) and i<=3*n//4)   and not(i==0 and j==n-1) and not (i==n//4 and j==3*n//4) and not (i==n//2 and j==n//2) and not (i==3*n//4 and j==n//4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern66(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j<n-1 and i-j<=0 and i>0  ) and not ( i==0 and j==0) and not (j==n//4 and i==n//4)  and not(i==n//2 and j==n//2)  and not (j==3*n//4 and i==3*n//4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern72(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern73(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1:
                print("*",end=" ")
            elif i>n//4 and i<3*n//4 and j>n//4 and j<3*n//4:
                print("#",end=" ")
            else:
                print(end="  ")
        print()

def Pattern74(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or i==n-1 or i-j==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern75(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1 or i-j==0 or i+j==n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Fibonacci(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1:
        return Fibonacci(n-1)+Fibonacci(n-2)

def Pattern76(n):
    n=n|1
    temp=0
    for i in range(n):
        for j in range(n):
            if i-j>=0:
                print(Fibonacci(temp),end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern77(n):
    n=n|1
    for i in range(n):
        temp=0
        for j in range(n):
            if i-j>=0:
                print(temp,end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern78(n):
    n=n|1
    temp=1
    for i in range(n):
        for j in range(n):
            if i-j>=0:
                print(temp,end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern79(n):
    n=n|1
    for i in range(n):
        temp=i+1
        for j in range(n):
            if i-j>=0:
                print(temp,end=" ")
                temp+=n-j-1
            else:
                print(end="  ")
        print()

def Pattern80(n):
    n=n|1
    for i in range(n):
        if (i+1)%2==1:
            temp=1
        else:
            temp=2
        for j in range(n):
            if i-j>=0:
                print(temp,end=" ")
                temp+=2
            else:
                print(end="  ")
        print()

def Pattern81(n):
    n=n|1
    temp2=0

    for i in range(n):
        temp2+=i+1
        temp3=temp2
        for j in range(n):
            if i-j>=0:
                print(temp3,end=" ")
                temp3-=1
            else:
                print(end="  ")
        print()

def Pattern83(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j>=0 and i+j<n-1 :
                print(chr(65+j),end=" ")
            else:
                print(end="  ")
        print()

def Pattern84(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ((i-j>((n-1)//2) or i+j>=3*(n-1)//2) and (i>=n//2) and j<n//2) or ((j==n//4 or j==n//2) and i>=n//4) and not (j==n//2 and i==n//4):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern85(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ( (i+j<(n-1)//2) and (i<=n//2) and j<n//2) or ((i==n//4 or i==n//2) and j<=3*n//4) and not (i==n//2 and j==3*n//4):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern86(n):
    for i in range(n):
        temp=1
        for j in range(n):
            if (j)%2==1:
                print(temp,end=" ")
                temp+=1
            else:
                print(i+1,end=" ")
        print()

def Pattern87(n):
    for i in range(n):
        temp=1
        for j in range(n):
            if (j)%2==0:
                print(temp,end=" ")
                temp+=1
            else:
                print(i+1,end=" ")
        print()

def Pattern88(n):
    for i in range(n):
        for j in range(n):
            if i+j==n//2 or i-j==(-(n-1)//2) or i+j==3*(n-1)//2 or i-j==n//2 or i==n//2 or j==n//2:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern89(n):
    for i in range(n):
        for j in range(n):
            if (i-j==(-(n-1)//2) and not i==0) or (i+j==3*(n-1)//2 and not i==n-1) or  i==n//2 :
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern90(n):
    for i in range(n):
        for j in range(n):
            if not(i+j>n//2 and i-j>(-(n-1)//2) and i+j<3*(n-1)//2 and i-j<n//2) :
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern91(n):
    for i in range(n):
        for j in range(n):
            if not(i+j>n//2 and i-j>(-(n-1)//2) and i+j<3*(n-1)//2 and i-j<=0 and j>n//4 and i<3*n//4) :
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern93(n):
    for i in range(n):
        for j in range(n):
            if (i+j>=n//2 and i-j>=(-(n-1)//2) and i+j<=3*(n-1)//2 and i-j<=n//2 and i>=n//4 and i<=3*n//4 )  and not (j==0 or j==n-1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern94(n):
    for i in range(n):
        for j in range(n):
            if not((i>n//4 and i<2*n//5 and j>n//4) or (i>6*n//10 and i<3*n//4 and j<3*n//4)  or i==0 or i==n-1 or j==0 or j==n-1) :
                print("*",end="  ")
            else:
                print(end="   ")
        print()

# def Pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if ((j<=n//2 and i<=n//2) or (i<=n//4 and j<=3*n//4) or (i<=3*n//4 and j<=n//4)) and not(i==0 or j==0):
#                 print("*",end=" ")
#             else:
#                 print(end="  ")
#         print()