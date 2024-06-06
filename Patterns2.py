def Pat_A(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ((i<=(n-1)//2) and ((i-j>=-(n-1)//2 and i+j>=(n-1)//2) and (i-j==-(n-1)//2 or i+j==(n-1)//2 or i==n//4))):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_B(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i*j==0 or j==n//2 or i==n//2 or i==n-1)and (j<=n//2):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()
def Pat_C(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0  or i==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_D(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j<=n//2)and(i*j==0 or j==n//2 or i==n-1):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_E(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or i==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_F(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0  or i==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_G(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i*j==0 )   or (j<=n//2 and i==n-1) or((i>=n//2 and j>=n//2) and (i==n//2  or j==n//2 or j==n-1 ) ):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_H(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_I(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0 or  i==n-1 or j==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_J(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0 or i-j==n//2 or j==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_K(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or i-j==n//2 or i+j==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_L(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or i==n-1 :
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_M(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j==0 or j==n-1) or (i<=n//2 and (i-j==0 or i+j==n-1)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_N(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i-j==0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_O(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or j==n-1 or i==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_P(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or ((i<=n//2) and (j==n-1 or j==0  or i==0 or i==n//2)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_Q(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i*j==0 or j==n-1 or i==n-1) or ((i>n//2 and j>=n//2)  and( i-j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_R(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or ((i<=n//2) and (j==n-1 or j==0  or i==0 or i==n//2)) or ((i>=n//2 and j>=n//2)  and( i-j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_S(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1 or i==n//2) or ((i<=n//2) and (i==0 or j==0 )) or ((i>=n//2) and (i==n-1 or j==n-1 )):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_T(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0 or j==n//2 :
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_U(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_V(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ((i>=(n-1)//2) and (i-j==(n-1)//2 or i+j==3*(n-1)//2)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_W(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (j==0 or j==n-1) or (i>=n//2 and (i-j==0 or i+j==n-1)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_X(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j==0  or i+j==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_Y(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ((i<=n//2) and ( i+j==n-1 or i-j==0)) or ((i>=n//2) and (j==n//2)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_Z(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0 or i+j==n-1 or i==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_0(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i*j==0 or j==n-1 or i==n-1 or i-j==0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_1(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==n-1 or j==n//2or i+j==(n//2):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_2(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i==0 or i+j==n-1 or i==n-1) or ((i<n//2) and (j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_3(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0  or i==n-1 or((j>=n//2) and (i+j==n-1 or i-j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_4(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==n//2 or ((i>=n//2) and ( j==n-1) )   or ((i<=n//2) and(j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_5(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==n//2 or i==0  or i==n-1 or((i>=n//2) and ( j==n-1) )   or ((i<=n//2) and(j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_6(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==n//2 or i==0  or i==n-1 or((i>=n//2) and ( j==n-1) )  or j==0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_7(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0  or i+j==n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_8(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==n-1 or j==n-1 or i==n//2 or i*j==0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pat_9(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i==0 or i==n//2  or j==n-1 or ((i<=n//2) and (j==0)):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_1(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j>=0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_2(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i+j>=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_3(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i+j<=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_4(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j<=0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_5(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j<(-((n-1)//2)) or i+j<(n-1)//2 or i-j>(n-1)//2 or i+j>3*(n-1)//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_6(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i-j==(-((n-1)//2)) or i+j==(n-1)//2 or i-j==(n-1)//2 or i+j==3*(n-1)//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_7(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i-j>=0:
                print(j,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_8(n):
    temp=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i-j>=0:
                print(temp,sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Patt_9(n):
    temp=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i-j>=0:
                if temp//10==1:
                    temp+=1
                temp=temp%10
                print(temp,sep="",end=" ")
                temp+=1
                # print(temp)
            else:
                print(end="  ")
        print()

def Patt_10(n):
    # temp=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i-j>=0 and i+j<=n-1:
                print(j,sep="",end=" ")
                # temp+=1
            else:
                print(end="  ")
        print()

def Patt_11(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if i+j<=n-1:
                print(chr(65+i),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Patt_12(n):
    n=n|1
    for i in range(n):
        temp=0
        for j in range(n):
            if i<=n//2 and i+j>=n//2  and i-j>=-(n//2):
                print(chr(65+temp),sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Patt_13(n):
    n=n|1
    for i in range(n):
        temp=0
        for j in range(n):
            if i<=n//2 and i+j>=n//2  and i-j>=-(n//2):
                print(chr(65+temp),sep="",end=" ")
                if(j<n//2):
                    temp+=1
                if(j>=n//2):
                    temp-=1
            else:
                print(end="  ")
        print()

def Patt_14(n):
    n=n|1
    for i in range(n):
        temp=0
        for j in range(n):
            if (i<=n//2 and i+j>=n//2  and i-j>=-(n//2))  or ((i>(n-1)//2 and i+j<=3*(n-1)//2 and i-j<=(n-1)//2)):
                print(chr(65+temp),sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Patt_15(n):
    n=n|1
    for i in range(n):
        if i<=n//2:
            temp=2*i
        else:
            temp=(i%(n//2))+(n-i-1)
        for j in range(n):
            if (i<=n//2 and i+j>=n//2  and i-j>=-(n//2)):
                print(chr(65+temp),sep="",end=" ")
                temp-=1

            elif ((i>=(n-1)//2 and i+j<=3*(n-1)//2 and i-j<=(n-1)//2)):
                print(chr(65+temp),sep="",end=" ")
                temp-=1
            else:
                print(end="  ")
        print()

def Patt_16(n):
    n=n|1
    for i in range(n):
        temp=0
        for j in range(n):
            if i<=n//2 and i+j>=n//2  and i-j>=-(n//2) or ((i>=(n-1)//2 and i+j<=3*(n-1)//2 and i-j<=(n-1)//2)):
                print(chr(65+temp),sep="",end=" ")
                if(j<n//2):
                    temp+=1
                if(j>=n//2):
                    temp-=1
            else:
                print(end="  ")
        print()

def Pattern1(n):
    for i in range(n):
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern2(n):
    for i in range(n):
        temp=n//2
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(temp,sep="",end=" ")
                temp-=1
            else:
                print(end="  ")
        print()

def Pattern3(n):
    for i in range(n):
        if(i<=n//2):
            temp=n//2-i
        else:
            temp=n//2-(n-i-1)
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(temp,sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern4(n):
    for i in range(n):
        temp=n//2
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(chr(65+temp),sep="",end=" ")
                temp-=1
            else:
                print(end="  ")
        print()

def Pattern5(n):
    for i in range(n):
        if(i<=n//2):
            temp=n//2-i
        else:
            temp=n//2-(n-i-1)
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(chr(65+temp),sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern6(n):
    for i in range(n):
        for j in range(n):
            if i-j<=0 and i+j>=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()
def Pattern7(n):
    for i in range(n):
        temp=n//2
        for j in range(n):
            if i-j<=0 and i+j>=n-1:
                print(temp,sep="",end=" ")
                temp-=1
            else:
                print(end="  ")
        print()
def Pattern8(n):
    for i in range(n):
        if(i<=n//2):
            temp=n//2-i
        else:
            temp=i-n//2
        for j in range(n):
            if i-j<=0 and i+j>=n-1:
                print(temp,sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern9(n):
    for i in range(n):
        if(i<=n//2):
            temp=n//2-i
        else:
            temp=i-n//2
        for j in range(n):
            if i-j<=0 and i+j>=n-1:
                print(chr(65+temp),sep="",end=" ")
                temp+=1
            else:
                print(end="  ")
        print()

def Pattern10(n):
    for i in range(n):
        temp=n//2
        for j in range(n):
            if i-j<=0 and i+j>=n-1:
                print(chr(65+temp),sep="",end=" ")
                temp-=1
            else:
                print(end="  ")
        print()

def Pattern11(n):
    for i in range(n):
        temp=" "*(n-i)
        print(temp,end="")
        for j in range(n):
            if i-j>=0:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern12(n):
    for i in range(n):
        temp=" "*(n-i)
        print(temp,end="")
        for j in range(n):
            if i-j>=0:
                print(i+1,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern13(n):
    for i in range(n):
        temp=" "*(n-i)
        print(temp,end="")
        temp2=1
        for j in range(n):
            if i-j>=0:
                print(temp2,sep="",end=" ")
                temp2+=1
            else:
                print(end="  ")
        print()

def Pattern14(n):
    for i in range(n):
        temp=" "*(n-i)
        print(temp,end="")
        for j in range(n):
            if i-j>=0:
                print(chr(65+i),sep="",end=" ")
            else:
                print(end="  ")
        print()
def Pattern15(n):
    for i in range(n):
        temp=" "*(n-i)
        print(temp,end="")
        temp2=1
        for j in range(n):
            if i-j>=0:
                print(chr(65+temp2-1),sep="",end=" ")
                temp2+=1
            else:
                print(end="  ")
        print()



def Pattern16(n):
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern17(n):
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print(n-i,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern18(n):
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print(n-j,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern19(n):
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print(chr(65+n-i-1),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern20(n):
    temp2=1
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print(chr(65+n-j-temp2),sep="",end=" ")

            else:
                      print(end="  ")
        temp2+=1
        print()

def Pattern21(n):
    for i in range(n):
        temp=" "*i
        print(temp,end="")
        for j in range(n):
            if i+j<=n-1:
                print(chr(65+j),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern22(n):
    for i in range(n):
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
        else:
            for k in range(i):
                print(end=" ")
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern23(n):
    n=n|1
    temp=1
    for i in range(n):
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
        else:
            for k in range(i):
                print(end=" ")
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(temp,sep="",end=" ")
            else:
                print(end="  ")
        if i<n//2:
            temp+=1
        else:
            temp-=1
        print()

def Pattern24(n):
    n=n|1
    for i in range(n):
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
            temp=1
        else:
            for k in range(i):
                print(end=" ")
            temp=i-n//2
        for j in range(n):
            if i-j>=0 and i+j<=n-1 and i<=n//2:
                print(temp,sep="",end=" ")
                temp+=1
            elif i-j>=0 and i+j<=n-1 and i>n//2:
                print(temp+1,end=" ")
                temp+=1

            else:
                print(end="  ")

        print()

def Pattern25(n):
    n=n|1
    for i in range(n):
        temp=1
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
        else:
            for k in range(i):
                print(end=" ")
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(temp,sep="",end=" ")
                temp+=1

            else:
                print(end="  ")

        print()


def Pattern26(n):
    n=n|1
    temp=1
    for i in range(n):
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
        else:
            for k in range(i):
                print(end=" ")
        for j in range(n):
            if i-j>=0 and i+j<=n-1:
                print(chr(65+temp-1),sep="",end=" ")
            else:
                print(end="  ")
        if i<n//2:
            temp+=1
        else:
            temp-=1
        print()

def Pattern27(n):
    n=n|1
    for i in range(n):
        if i<=n//2:
            for k in range(n-i-1):
                print(end=" ")
            temp=1
        else:
            for k in range(i):
                print(end=" ")
            temp=i-n//2
        for j in range(n):
            if i-j>=0 and i+j<=n-1 and i<=n//2:
                print(chr(65+temp-1),sep="",end=" ")
                temp+=1
            elif i-j>=0 and i+j<=n-1 and i>n//2:
                print(chr(65+temp),end=" ")
                temp+=1

            else:
                print(end="  ")

        print()

def Pattern28(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-(n//2) or i+j==n//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern29(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-(n//2) or i+j==n//2:
                print(i+1,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern30(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-(n//2) or i+j==n//2:
                print((n//2+1)-i,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern31(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-(n//2) or i+j==n//2:
                print(chr(65+i),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern32(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-(n//2) or i+j==n//2:
                print(chr(65+(n//2)-i),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern33(n):
    for i in  range(n):
        for j in range(n):
            if i-j==((n-1)//2) or i+j==3*(n-1)//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern34(n):
    for i in  range(n):
        for j in range(n):
            if i-j==((n-1)//2) or i+j==3*(n-1)//2:
                print((i+1)-n//2,sep="",end=" ")
            else:
                print(end="  ")
        print()
def Pattern35(n):
    for i in  range(n):
        for j in range(n):
            if i-j==((n-1)//2) or i+j==3*(n-1)//2:
                print(n-i,sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern36(n):
    for i in  range(n):
        for j in range(n):
            if i-j==((n-1)//2) or i+j==3*(n-1)//2:
                print(chr(65+(i)-n//2),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern37(n):
    for i in  range(n):
        for j in range(n):
            if i-j==((n-1)//2) or i+j==3*(n-1)//2:
                print(chr(65+(n-i)-1),sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern38(n):
    for i in  range(n):
        for j in range(n):
            if i-j==-((n-1)//2) or i-j==((n-1)//2) or i+j==n//2 or i+j==3*(n-1)//2:
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern39(n):
    temp=1
    for i in  range(n):
        for j in range(n):
            if i-j==-((n-1)//2) or i-j==((n-1)//2) or i+j==n//2 or i+j==3*(n-1)//2:
                if(i<=n//2):
                    print(temp,sep="",end=" ")

                else:
                    print(n-temp+1,sep="",end=" ")


            else:
                print(end="  ")
        temp+=1
        print()

def Pattern40(n):
    temp=n//2+1
    for i in  range(n):
        for j in range(n):
            if i-j==-((n-1)//2) or i-j==((n-1)//2) or i+j==n//2 or i+j==3*(n-1)//2:
                if(i<=n//2):
                    print(temp,sep="",end=" ")

                else:
                    print(n//4-temp ,sep="",end=" ")
            else:
                print(end="  ")
        temp-=1
        print()

def Pattern41(n):
    temp=1
    for i in  range(n):
        for j in range(n):
            if i-j==-((n-1)//2) or i-j==((n-1)//2) or i+j==n//2 or i+j==3*(n-1)//2:
                if(i<=n//2):
                    print(chr(65+temp-1),sep="",end=" ")

                else:
                    print(chr(65+n-temp),sep="",end=" ")


            else:
                print(end="  ")
        temp+=1
        print()

def Pattern42(n):
    temp=n//2+1
    for i in  range(n):
        for j in range(n):
            if i-j==-((n-1)//2) or i-j==((n-1)//2) or i+j==n//2 or i+j==3*(n-1)//2:
                if(i<=n//2):
                    print(chr(65+temp-1),sep="",end=" ")

                else:
                    print(chr(65+n//4-temp-1) ,sep="",end=" ")
            else:
                print(end="  ")
        temp-=1
        print()

def Pattern43(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i-j<=(-(n//2)) or i+j<=n//2) and (i<=n//2):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern44(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i-j>=((n-1)//2) or i+j>=3*(n-1)//2) and (i>=n//2):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern45(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if (i-j>=0 and i+j<=n-1 and j<=n//2) or (i-j<=0 and i+j>=n-1 and j>=n//2):
                print("*",sep="",end=" ")
            else:
                print(end="  ")
        print()

def Pattern46(n):
    n=n|1
    for i in range(n):
        for j in range(n):
                if (i+j>=n-1):
                    print(" * ",end=" ")
                else:
                    print(" ",end=" ")
        for j in range(n):
            if (i+j>=n-1):
                print(" * ",end=" ")
            else:
                print("   ",end=" ")
        print()

def Pattern48(n):
    for i in range(n):
        for j in range(n):
            if (i-j>=0 and i+j>=n-1 and i>=n//2) and not (i-j<(n-1)//2 and i+j<3*(n-1)//2 and i>=3*n//4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern49(n):
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern50(n):
    temp=1
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1):
                print(temp,end=" ")
            else:
                print(end="  ")

        temp+=1
        print()

def Pattern51(n):
    temp=n
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1):
                print(temp,end=" ")
            else:
                print(end="  ")

        temp-=1
        print()

def Pattern52(n):
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1)  :
                print(j+1,end=" ")

            else:
                print(end="  ")
        print()

def Pattern53(n):
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1)  :
                print(n-j,end=" ")

            else:
                print(end="  ")
        print()

def Pattern54(n):
    temp=1
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1):
                print(chr(65+temp-1),end=" ")
            else:
                print(end="  ")
        temp+=1
        print()

def Pattern55(n):
    for i in range(n):
        for j in range(n):
            if (i-j==0 or i+j==n-1)  :
                print(chr(65+j),end=" ")

            else:
                print(end="  ")
        print()

def Pattern56(n):
    for i in range(n):
        for j in range(n):
            if i-j==0:
                print("o",end=" ")
            else:
                print("*",end=" ")
        print()

def Pattern57(n):
    for i in range(n):
        for j in range(n):
            if i-j<=0:
                print("o",end=" ")
            else:
                print("*",end=" ")
        print()

def Pattern58(n):
    for i in range(n):
        for j in range(n):
            if i-j==0 or i+j==n-1:
                print("*",end=" ")
            else:
                print("o",end=" ")
        print()

def Pattern59(n):
    for i in range(n):
        for j in range(n):
            if i-j==0 and i+j==n-1:
                print("o",end=" ")
            else:
                print("*",end=" ")
        print()

def Pattern60(n):
    for i in range(n):
        for j in range(n):
            if i==n//2 or j==n//2:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern61(n):
    for i in range(n):
        for j in range(n):
            if i==n//2 or j==n//2:
                print("*",end=" ")
            else:
                print("o",end=" ")
        print()

def Pattern62(n):
    for i in range(n):
        for j in range(n):
            if i+j<n-1 and i+j>=n//2 and i<=n//2:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def Pattern63(n):
    for i in range(n):
        for j in range(n):
            if (j>=n//4 and i-j>=0)   and not (i==n//4 and j==n//4)   and not(i==n//2 and i-j==0) and not(i==3*n//4 and i-j==0) and not(i==n-1 and j==n-1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()