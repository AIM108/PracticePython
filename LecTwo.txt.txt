from asyncio.windows_events import NULL
from tkinter import Y
import numpy as np
from myfunction import testf
import matplotlib.pyplot as plt

##Functions in python
##Shallow copy and deep copy in python

def function1(A):
    print(A)
    A[0,0]=-2.0
    print(A)
def testfunction1():
    B =np.array([[5.0,2.0]])
    function1(B)
    print(B)

def function2(A):
    print(A)
    C=A.copy();
    C[0,0]=-2
    print(C)
    print(A)
def testfunction2():
    B=np.array([[5.0,2.0]])
    function2(B)
    print(B)

##Recursive Functions Algorithms
##AlgorithmOne factorial
def algoOneFactorial(n):
    if n == 0:
        return 1
    return n * algoOneFactorial(n -1)
def testAlgoOneFactorial():
    output= algoOneFactorial(5)
    print(output)
    ##Outcome should be 120

##AlgorithmTwo computing e to the power of x e=2.71828
def algorithmTwoEToThePowerOfX(powerfactor,iterations):
    term=1.0
    y=term
  
    for k in range(2,iterations):
        term =term*(powerfactor/(k-1))
        y =y+term
    return y
def testAlgoTwoFirstApproch():
    outputOne=algorithmTwoEToThePowerOfX(6,200)
    print(outputOne)
    ##Should be 403.42879, higher iterations get us closer to this number
    outputTwo=algorithmTwoEToThePowerOfX(-3,200)
    print(outputTwo)
    ##Should be .0497870684, higher iterations get us closer to this number

##AlgorithmThree second approch to e to the power of x

def getEpsilon():
    epsilon=1
    while epsilon+1.0>1.0:
        epsilon=epsilon/2.0
    return epsilon*2.0
def algorithmThreeToThePowerOfX(x,n):
    term=1.0
    y=term
    e=getEpsilon()
    diff=2*e
    k=2
    while diff > e and k < n:
        term= term*(x/(k-1))
        y=y+term
        diff = abs(term)
        k=k+1

    return y 
def testAlgoThree():
    outputOne=algorithmThreeToThePowerOfX(6,200)
    print(outputOne)
    ##Should be 403.42879, higher iterations get us closer to this number
    outputTwo=algorithmThreeToThePowerOfX(-3,200)
    print(outputTwo)
    ##Should be .0497870684, higher iterations get us closer to this number

##AlgorithmFour computing the prime numbers
def algorithmFourPrimeNumbersLessThanN(n):
    primesList=[2]
    primeListLength=1
    for x in range(3,n):
        flag=0
        for y in range(primeListLength):
            if (x%primesList[y])==0:
                flag =1
                break
        if flag ==0:
            primeListLength=primeListLength+1
            primesList.append(x)
    return primesList
def testAlgoFour():
    algorithmFourPrimeNumbersLessThanN(100)
##AlgorithmFive Unique Python features
def alogorithmFiveForElseLopp(n):
    primesList=[2]
    primeListLength=1
    for x in range(3,n):
        for y in range(primeListLength):
            if (x%primesList[y])==0:
                break
        else:
            primeListLength=primeListLength+1
            primesList.append(x)
    print(primesList)
def testAlgoFive():
    alogorithmFiveForElseLopp(100)
##Exercises
##Exercise one, compute n factorial
def exOne(n):
    if n == 0:
        return 1
    return n*exOne(n-1)
def testExOne():
    output=exOne(5) ##Should be 120
    print(output)

##Exercise Two
##FirstWay
def exTwoRecursion(x,n):
    if n==-1:
        return 0
    term=((x**(n+1))/(n+1))
    print(term)
    return term+ exTwoRecursion(x,(n-1))
def testExTwoRecursion():
    output=exTwoRecursion(.50,3)
    print("This was the recursive output:",output)
##SecondWay
def exTwoCycles(x,n):
    sum=0
    term=0
    for k in range(n+1):
        term= ((x**(k+1))/(k+1))
        sum=sum+term
        print(term)
    return sum
def testExTwoCycles():
    output=exTwoCycles(.50,3)
    print("This was the cycle output: ",output)
##Exercise Three Leibniz formula for pie
def exThreeComputePieLeibniz(n):
    sum=1
    term=0
    for k in range(1,n+1):
        if (k%2) != 0:
            term=(-((1/(1+(2*k)))))
        else:
            term=((1/(1+(2*k))))
        sum=sum+term
    return 4*sum
def testExThree():
    output=exThreeComputePieLeibniz(10)
    print(output)

##Exercise Three Machins formula for pie
def exThreeMachinsFormula(n):
    leftSum=(1/5)
    rigthSum=(1/239)
    leftterm=0
    rigthterm=0
    for k in range(1,n+1):
        if (k%2) != 0:
            leftterm=((-(1/(1+(2*k))))*(1/5)**(1+2*k))
            rigthterm=((-(1/(1+(2*k))))*(1/239)**(1+2*k))
        else:
            leftterm=((1/(1+(2*k)))*(1/5)**(1+2*k))
            rigthterm=((1/(1+(2*k)))*(1/239)**(1+2*k))
        leftSum=leftSum+leftterm
        rigthSum=rigthSum+rigthterm
    leftSum=(16*leftSum)
    rigthSum=(4*rigthSum)
    return (leftSum-rigthterm)
def testExThreeMachins():
    output=exThreeMachinsFormula(10)
    print(output)

##Exercise Four
def exdoublePrimeList(n):
    primeList=algorithmFourPrimeNumbersLessThanN(n)
    primeList_length=len(primeList)
    doublePrimeList=[2,3]
    k=2
    while k !=primeList_length-1:
        if(primeList[k+1]-primeList[k])==2:
            doublePrimeList.append(primeList[k])
            doublePrimeList.append(primeList[k+1])
            k=k+2
        else:
            k=k+1
    return doublePrimeList
def testExFour():
    output=exdoublePrimeList(100)
    print(output)

def main():
    ##testf()
    ##testfunction1()
    ##testfunction2()
    ##testAlgoOneFactorial()
    ##testAlgoTwoFirstApproch()
    ##testAlgoThree()
    ##testAlgoFour()
    ##testAlgoFive()
    ###testExOne()
    ##testExTwoRecursion()
    ##testExTwoCycles()
    ##testExThree()
    ##testExThreeMachins()
    testExFour()


if __name__ == "__main__":
    main()
