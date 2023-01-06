#@author :Alonso Montelongo
#@version : 1.0
#MATH-4340-001



import numpy as np
import copy as c
import pickle



#Advanced Problem
#Least squares solution when the A matrix does not have full column rank


#@name :QRImprovedDecomposition
#@param :Will take in a mxn matrix A, not nessasary linearly independent and a tolerance o e which will be a small number
#@return :mxp matrix Q, pxn matrix R, and the rank p of the matrix
def QRImprovedDecomposition(A):
    (m,n) =np.shape(A)

    #Initialize Q and R and the Rank
    R= np.zeros((n,n))
    Q =np.zeros((m,n))
    rank = 0
    tol=1e-7
    for j in range(0,n):
        vector_proj = np.zeros((m,1))
        for i in range(0,rank):
            #Vector projection plus the row i in q and r at i,j
            vector_proj =vector_proj+(R[i,j]*Q[:,i:i+1])
        #The diffrence in our actual A row j and its projection
        residual =A[:,j:j+1] - vector_proj
        norm_residual = np.linalg.norm(residual)
        
        
        # we will make e the tolerance a very small number
        
        if(norm_residual >= tol):
            rank = rank+1
            R[rank-1,j] =norm_residual
            Q[:,rank-1:rank] = (residual/norm_residual)

            for k in range(j+1,n):
                R[rank-1,k] = np.matmul((np.transpose(Q[:,rank-1:rank])),A[:,k:k+1])
    return Q,R,rank


#@name :forward
#@param : nxn matric L, rank n, and vector b of nx1
#@return : nx1 vector z that solves Lz =b
def forward(L,n,b):
    z =np.zeros((n,1))
    z[0:0+1] = b[0:0+1]/L[0:0+1,0:0+1]
    for i in range(1,n):
        # sum =0
        # for j in range(0,i):
        #     print("This is the sum during ",j, "sum= ",sum)
        #     sum =sum+(L[i:i+1,j:j+1]*z[j:j+1])
        sum = np.matmul(L[i,0:i],z[0:i,0])
        z[i] =(b[i]-sum)/(L[i,i]) #Their is a problem herer in its shape (0,0) (1,1) brodecast
    return z





#Will compute the solution to the least squares proble min ||AxLS-b||
#@name :LSQR
#@param :Takes in matrix mxn A, and vector b of mx1
#@return :x matrix to the LS of QR
def LSQR(A,b):
    (Q,R,rank) =QRImprovedDecomposition(A)
    Q= Q[:,0:rank]
    R =R[0:rank,:]
    QTrans =np.transpose(Q)
    b= np.matmul(QTrans,b)
    (Q1,R1,rank1) =QRImprovedDecomposition(np.transpose(R))
    z =forward(np.transpose(R1),rank,b)
    x =np.matmul(Q1,z)

    return x

#Will test our LSQR and give us an output
def TestForLSQRPorblems():
    #ExercisesTwo
    test =np.array([[1.,5,9],[2.,6,10],[3.,7,11],[4.,8,12]])
    print("This is my input matrix to the LSQR:\n",test)
    column =np.array([[1.],[2],[3],[4]])
    print("This is my input colum for LSQR:\n",column)
    x = LSQR(test,column)
    print("This is a test of my solution x:\n",x)



    #ExercisesThree
    testTwo =np.array([[1,2,3],[2,4,6]])
    print("This is my input matrix to the LSQR:\n",testTwo)
    columnTwo =np.array([[1],[1]])
    print("This is my input colum for LSQR:\n",columnTwo)
    y = LSQR(testTwo,columnTwo)
    print("This is a test of my solution y:\n",y)


    #ExercisesFour
    TestThree =np.array([[0,1,5,9,-1],[0,2,6,10,1],[0,3,7,11,1],[0,4,8,12,1]])
    print("This is my input matrix to the LSQR:\n",TestThree)
    columnThree =np.array([[1],[2],[3],[4]])
    print("This is my input colum for LSQR:\n",columnThree)
    z = LSQR(TestThree,columnThree)
    print("This is a test of my solution z:\n",z)






#Advance Proble
#Object oriented programming with classes in python
##Will print primeslist and indicate if its a double prime or not



#@class :primes, will be an object that contains a number, and a boolean to indicate whether it is a twin prime
class primes(object):
    def __init__(self,m,var):
        self.number = m
        self.twin = var

    def display(self,i):
        if self.twin == True:
            print("The twin prime", self.number, " is at index", i+1)
        else:
            print("The prime number ", self.number," is at index", i+1)
    def setTwin(self,var):
        self.twin =var

#@name :prime_generator
# @param :n, the range of prime numbers generated from 2 to n
# @return :primeslist, the list of prime numbers and length_primes, the length of the list    
def prime_generator(N):
    #find all prime numbers and double primes less than N
    primeslist =[]
    length_primes =2
    primeslist.append(primes(2,True))
    primeslist.append(primes(3,True))

    #This code bellow will generate the prime numbers and twin primes 
    
    for x in range(4,N):

        for i in range(length_primes):
            
            if( x%((primeslist[i]).number) ==0):
                break
            elif (i == (length_primes-1)):
                if((x-2)==(primeslist[length_primes-1].number)):
                    primeslist[length_primes-1].setTwin(True)
                    primeslist.append(primes(x,True))
                    length_primes =length_primes+1
                else:
                    primeslist.append(primes(x,False))
                    length_primes =length_primes+1
    return primeslist, length_primes

#Will test our primes_generator and give us an output
def test():
    primeslist, length_primes = prime_generator(50)
    for i in range(0,length_primes):
        primeslist[i].display(i)



def main():
    TestForLSQRPorblems()
    test()

if __name__ == "__main__":
    main()