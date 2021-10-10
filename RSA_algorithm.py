import random 
def euclidean_gcd(a,b):
    if b==0:
        return a
    else:
        return euclidean_gcd(b,a%b)

def euler_toitent(p, q):
    return (p-1)*(q-1)

def public_key_finder(phi,n):
    e=2
    list_e=[]
    while(e<phi):
        if euclidean_gcd(e,phi)==1:
            return (e,phi)
        e+=1

def private_key_calculator(e ,phi):
    i=1
    global n
    while(True):
        d=((phi*i)+1)/e
        if float(d).is_integer():
            return (int(d),n)
        i+=1
def encryption(p, e, n):
    power=pow(p,e[0])
    encrypted_num=power%n
    return encrypted_num

def decryption(c,d,n):
    power=pow(c,d[0])
    original_message=power%n
    return original_message

p=int(input("enter any number which is prime "))
q=int(input("enter any number which is prime and coprime with p "))
phi=euler_toitent(p,q)
n=p*q
public_key=public_key_finder(phi, n)
print("the public key calculated is ",public_key)
private_key=private_key_calculator(public_key[0],phi)
print("the private key calculated is ",private_key)
message=int(input("enter any number as message "))
encrypted_num=encryption(message , public_key, n)
print("the encrypted message at user side is ",encrypted_num)
plain=decryption(encrypted_num, private_key, n)
print("the original message received by receiver side is ",plain)