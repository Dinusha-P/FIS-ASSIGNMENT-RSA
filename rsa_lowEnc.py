'''
DEMONSTRATION OF LOW EXPONENT ATTACKON RSA
AUTHOR1 : DINUSHA P
AUTHOR2: DURGESH
DATE: 20/11/2022
'''

#Extended Euclidean Algorithm to find multiplicative inverse
def gcdExtended(a,b):   
    if(b==0):
        return a,1,0
    else:
        q=a//b
        r=a%b
        d,x,y=gcdExtended(b,r)
        return d,y,x-q*y

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,d,_=gcdExtended(e,r)
    if(gcd!=1):
        print("No inverse")
        return None
    else:
        if(d<0):
            #since s<0 s=s%r
            d=d%r
        elif(d>0):
            d=d
        return d%r

print("\n")

#calculate cube root
def cube_root(x):
        return x**(1/3)

c1=int(input("Enter cipher text1\n"))
n1=int(input("Enter modulus for first party\n"))
c2=int(input("Enter cipher text2\n"))
n2=int(input("Enter modulus for second party\n"))
c3=int(input("Enter cipher text3\n"))
n3=int(input("Enter modulus for third party\n"))
e=3

M=n1*n2*n3
M1=n2*n3
M2=n1*n3
M3=n1*n2
N1=mult_inv(M1,n1)
N2=mult_inv(M2,n2)
N3=mult_inv(M3,n3)

m=(M1*N1*c1+M2*N2*c2+M3*N3*c3)%M 
message=int(cube_root(m))
#message
print(message)

