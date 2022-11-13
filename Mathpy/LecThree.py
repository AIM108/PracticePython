##This will contain the code for Crytography
import numpy as n

##Will give us the GCD of two integer numbers
def EuclideanAlgorithmGCD(a,b):
    remander=0
    while (a%b)>0:
        remander=a%b
        a=b
        b=remander
    return b
def testEuclideanAlgorithmGCD(a,b):
    GCD=EuclideanAlgorithmGCD(a,b)
    print("The GCD of ",a," and ",b,"is :",GCD)


##Extended Euclidean Algorithm
def gcd(a,p):
    (oldr,r) = (a,p)
    (olds,s) = (1,0)
    (oldt,t) = (0,1)

    while r !=0:
        q=n.floor(oldr//r)
        (oldr,r) =(r,oldr-(q*r))
        (olds,s) =(s,olds-(q*s))
        (oldt,t) =(t,oldt-(q*t))
    if olds < 0:
        olds=olds+p
    return oldr,olds

def testgcd(a,b):
    (g,s) = gcd(a,b)
    print("The GCD useing EEA: ",g," and the multiplicity of ",a," is: ",s)




def exerciseOne():
    ##Check using this equation  m^k modN =(m modN)^k  modN
    m=13
    k=2
    N=5

    ## 13**2=169 , 169 mod5=4
    ## 13 mod5 =3, 3**2 =9 ,9 mod5 = 4

    if((m**k) %N) ==(((m%N)**k)%N):
        print("Equation for exerciseOne checks out")

def exrciseTwo():

    ##Chck Fermats little theorem: if m and p are relatively prime then ...... m^p = m modp......in other words m^(p-1) = 1 modp

    m=13
    p=5

    x=((m**p) == m%p)
    print(x)
    y=((m**(p-1))== 1%p)
    print(y)

def findD(landa,e):
    a=landa; q=1; r=landa
    while a!=1:
        b=e
        e=a-((a//b)*b)
        lastq=q
        q=r-(q*(a//b))
        r=lastq
        if r<0:
            r=r%landa
        a=b
    return r

def exrciseThree():
    p=61
    q=53 
    e=17
    N=p*q
    landa =(p-1)(q-1)

    ##find d, the decription 


    x= (42**e)%N
    y= (2667**2753)%N
    print(x)
    print(y)    





def main():
    ##testEuclideanAlgorithmGCD(5,10)
    ##testgcd(5,21)
    ##exerciseOne()
    ##exrciseTwo()
    print(findD(3233,17))
    print((42**17)%3233)
    print((2557**2753)%3233)
    ##exrciseThree()

if __name__ =="__main__":
    main()