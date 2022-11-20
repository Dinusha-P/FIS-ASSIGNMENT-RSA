'''
DEMONSTRATION OF RSA ATTACK BY FACTORIZATION OF PUBLIC KEY 
AUTHOR1 : DINUSHA P
AUTHOR2: DURGESH
DATE: 19/11/2022
'''

import random
import math
#factorization of input modulus
def factorization(n,ri): 
    # no prime divisor for 1
    if (n == 1):
        return n 
    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2
    while(1):
      # we will pick from the range [2, N)
      rj = ri #j < i
      ri = random.randint(2, n)
      d = math.gcd(abs(ri - rj), n)
      if (d > 1):
        break
    return d

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
            print("Value of d=%d."%(d%r))
        elif(d>0):
            print("Value of d=%d."%(d))
        return d%r

print("\n")

#n = 7727*7741
n=int(input("Enter modulus n\n"))
p=factorization(n,random.randint(2, n))
print("p= ",p)

q=int(n/p )
print("\nq=",q)

e=int(input("Enter value of e\n"))

#Eulers Toitent function calculation

phi= (p-1)*(q-1)
print("Eulers Toitent phi=",phi)
print("\n")

#Private Key calculation(d)
d = mult_inv(e,phi)