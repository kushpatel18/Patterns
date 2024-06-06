def PatternLA(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
    print("\n")

def PatternLD(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
    print("\n")
def PatternRA(n):
    str="* "
    str_emp="  "
    for i in range(0,n+1):
        str*=i
        for j in range(n-(i-1),0,-1):
            str_emp*=j
            print(str+str_emp)
            break
        str="* "
        str_emp="  "
    print("\n")
def PatternRD(n):
    str="* "
    str_emp="  "
    for i in range(0,n+1):
        str_emp*=i
        for j in range(n-i,0,-1):
            str*=j
            print(str_emp+str)
            break
        str="* "
        str_emp="  "
    print("\n")

def PatternMA(n):
    str="* "
    str_emp=" "
    for i in range(0,n+1):
        str*=i
        for j in range(n-(i-1),0,-1):
            str_emp*=j
            print(str_emp+ str)
            break
        str="* "
        str_emp=" "
    print("\n")

def RLine(n):
    str="*"
    str2=" "

    for i in range(0,n):
        str2*=i
        print(str2+str)

def Pattern_Mix(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i<=n//2 and i+j>=n//2  and i-j>=-(n//2):
                print("*",sep=" ",end=" ")

            else:
                print(end="  ")
        print()

def Pattern_Mix1(n):
    n=n|1
    for i in range(0,n):
        for j in range(0,n):
            if  (i==n-1 or j==n-1  or i*j==0) or ((j>=n//2 and i>=n//4 and i+j<=n-1) and (j==n//2 or i+j==n-1  or i-j==0)) or ((j>=n//2 and i<=3*n//4 and i-j>=0) and (j==n//2 or i+j==n-1  or i-j==0)):
                print("*",sep=" ",end="  ")

            else:
                print(end="   ")
        print()

n=int(input("Enter the no. of rows: "))
Pattern_Mix(n)