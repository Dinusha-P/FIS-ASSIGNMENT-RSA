import time
import random
import math
import matplotlib.pyplot as plt
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

timeList=[]
nList=[]

#n = 7727*7741
while(1):
  print("\n1.Do factorization for new N\n2.Exit\nEnter your choice : ")
  choice=int(input())
  if(choice==1):
    n=int(input("Enter modulus n\n"))
    startTime=time.time()
    p=factorization(n,random.randint(2, n))
    endTime=time.time()
    timeList.append((endTime-startTime)*10**3)
    nList.append(n.bit_length())
    print("p= ",p)
    q=int(n/p)
    print("\nq=",q)
    e=int(input("Enter value of e\n"))        
    phi= (p-1)*(q-1)
    print("Eulers Toitent phi=",phi)
    print("\n")    
    #Private Key calculation(d)
    d = mult_inv(e,phi)
  else:
    break
plt.xlabel('Length of modulus(in bits)')
plt.ylabel('Time(in ms)')
plt.plot(nList, timeList)
print(timeList,nList)

'''
[0.016689300537109375, 0.024318695068359375, 0.022649765014648438, 0.19478797912597656, 0.156402587890625, 0.09274482727050781, 0.7781982421875, 8.763790130615234, 18.098115921020508, 41.22734069824219, 106.0032844543457]
 [3, 6, 8, 12, 16, 17, 20, 24, 27, 31, 34]
 '''