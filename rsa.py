'''
RSA IMPLEMENTATION IN PYTHON
 
AUTHOR1 : DINUSHA P
AUTHOR2: DURGESH
DATE: 18/11/2022
'''
 
import math
import random
 
 
#Check if p and q are prime
def check_prime(num):
    if(num==2):
        return True
    elif((num<2) or ((num%2)==0)):
        return False
    elif(num>2):
        for i in range(2,num):
            if (num%i)==0:
                return False
    return True
 
 
#CALCULATION OF GCD FOR 'e' CALCULATION
def gcd(e,r):
    if(r==0):
        return e
    else:
        return gcd(r,e%r)
 
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
 
#Input prime numbers p and q
print("Please select 2 prime numbers\n")
p = int(input("Enter first prime number p: "))
q = int(input("Enter second prime number q: "))
print("\n")

if((check_prime(p)==False)or(check_prime(q)==False)):
    print("p and q should be prime\n")
    exit(0)
#Modulus calculation
n = p * q
print("RSA Modulus n=",n)
 
#Eulers Toitent function calculation

phi= (p-1)*(q-1)
print("Eulers Toitent phi=",phi)
print("\n")
 
#e Value Calculation
#Choose e randomly and and repeat random choice until e is coprime to phi(n)
e = random.randint(2, phi - 1)
while(gcd(e,phi)!=1):
    e = random.randint(2, phi - 1)
print("The value of e is:",e)
print("\n") 
#Private Key calculation(d)
d = mult_inv(e,phi)
print("\n")
#public and private keys
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("\n")
 
#Encryption
def encrypt(pub_key,plain_text):
    e,n=pub_key
    cipher_text=[]
    m=0
    for i in plain_text:
        if(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            cipher_text.append(c)
        elif(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            cipher_text.append(c)
        elif(i.isspace()):
            cipher_text.append(500)
    return cipher_text
     
 
#Decryption
def decrypt(priv_key,cipher_text):
    d,n=priv_key
    txt=cipher_text.split(',')
    plain_text=''
    m=0
    for i in txt:
        if(i=='500'):
            plain_text+=' '
        else:
            m=(int(i)**d)%n
            m+=97   
            c=chr(m)
            plain_text+=c
    return plain_text
 

#Choose Encryption or Decryption
while(1):    
    choose = input("Type '1' for encryption  '2' for decrytion and 3 to exit\n")
    if(choose=='1'):
        #Message
        message = input("Enter message to be encrypted\n")
        enc_msg=encrypt(public,message)
        print("Your encrypted message is:",enc_msg)
    elif(choose=='2'):
        #Message
        cipherText = input("Enter cipher text to be decrypted(Put ',' for separating numbers for decryption):")
        print("Your decrypted message is:",decrypt(private,cipherText))
    elif(choose=='3'):
        exit(0)
    else:
        print("You entered the invalid option.")
