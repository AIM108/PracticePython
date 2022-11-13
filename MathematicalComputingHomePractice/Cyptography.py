# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:40:18 2022

@author: alonmont
"""
import numpy as n
##AlgoOne
 
def gcd(a,p):
    
    (oldr,r) = (a,p)
    (olds,s) = (1,0)
    (oldt,t) = (0,1)
    
    while r != 0:
        print("oldr: ",oldr," r: ",r)
        q= n.floor(oldr//r)
        print(q)
        (oldr,r) = (r,oldr-q*r)
        (olds,s) = (s,olds - q*s)
        (oldt, t) = (t,oldt-q*t)
    if olds <0:
        olds =olds+p
    return oldr,olds,oldt

def testgcd():
    oldr,olds,oldt =gcd(222,1023)
    print("GCD: ")
    print(oldr)
    print(olds)
    print(oldt)

    
def algoOne(a,p):
    flag= True
     
    
    r,s= gcd(a,p)
    print("Inverse: ")
    print(r)
    print(s)
    
    if (r != 1):
        flag =False
    else:
        flag =True
    
    return s,flag

    
def testAlgoOne():
    s,flag =algoOne(3,7)    
    

    
    
def main():
    ##testAlgoOne()
    testgcd()
    
    
if __name__ == "__main__":
    main()