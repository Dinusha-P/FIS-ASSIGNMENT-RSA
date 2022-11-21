
'''
DEMONSTRATION OF LOW EXPONENT ATTACK ON RSA 
AUTHOR1 : DINUSHA P
AUTHOR2: DURGESH
DATE: 21/11/2022
'''

import math
import random
 
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
        return math.ceil(x**(1/3))
#Message to be sent
#e=3 is popular choice for e
e=3
plain_text=input("Enter message\n")
#msg=  bytes_to_long(plain_text.encode()
length=len(plain_text)
print(length)
plain_text=bytes(plain_text, 'utf-8')
msg = int.from_bytes(plain_text, "big")
print(msg)
#Compute cipher text for first party
p=int(input("Enter prime number 1\n"))
q=int(input("Enter prime number2\n"))
n1=p*q
print("n1=",n1)
c1=(msg**e)%n1
#Compute cipher text for second party
p=int(input("Enter prime number 1\n"))
q=int(input("Enter prime number2\n"))
n2=p*q
print("n2=",n2)
c2=(msg**e)%n2
#Compute cipher text for 3rd party
p=int(input("Enter prime number 1\n"))
q=int(input("Enter prime number2\n"))
n3=p*q
print("n3=",n3)
c3=(msg**e)%n3

M=n1*n2*n3
M1=n2*n3
M2=n1*n3
M3=n1*n2
N1=mult_inv(M1,n1)
N2=mult_inv(M2,n2)
N3=mult_inv(M3,n3)

m=(M1*N1*c1+M2*N2*c2+M3*N3*c3)%M 
message=int(cube_root(m))
#message m
print(message,"\n")
bytes_val = message.to_bytes(length, 'big')
print(f"Original message:",bytes_val)


'''

import math
import random
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
'''
