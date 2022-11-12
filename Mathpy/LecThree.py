##This will contain the code for Crytography

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



def eeagcd(a,p):
    (oldr,r) = (a,p)
    (olds,s) = (1,0)
    (oldt,t) = (0,1)

    while r !=0:
        q=oldr/r
        (oldr,r) =(r,oldr-(q*r))
        (olds,s) =(s,olds-(q*s))
        (oldt,t) =(t,oldt-(q*r))
    if olds < 0:
        olds=olds+p
    return oldr,olds


def main():
    testEuclideanAlgorithmGCD(1220,516)

if __name__ =="__main__":
    main()