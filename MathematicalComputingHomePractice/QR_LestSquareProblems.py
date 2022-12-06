import numpy as np
import copy as c



##AlgorithmOne, will get us the simple QR decomposition of matrix A, fully tested

def SimpleQRDecomposition(A):
    (m,n) = np.shape(A)
    R = np.zeros((m,n))
    Q = np.zeros((m,n))
   
    R[0,0]=np.linalg.norm(A[:,0:1])
    Q[:,0:1] = (A[:,0:1])/R[0,0]
    
    for k in range(1,n):
        vector_proj = np.zeros((m,1))
        for i in range(0,k):
            R[i,k] =np.matmul(np.transpose(Q[:,i:i+1]),A[:,k:k+1])
            vector_proj =vector_proj+(R[i,k]*Q[:,i:i+1])
            residual = A[:,k:k+1]-vector_proj
        R[k,k] = np.linalg.norm(residual)
        Q[:,k:k+1] = (residual/(R[k:k+1,k:k+1]))
    return Q,R

##This will return a nx1 vector x that solves Ux=z , fully tested 
def Backward(U,z):
    (m,n) =np.shape(U)
    print("This is my matrix:\n",U)
    print("This is my colum:\n",z)
    x= np.zeros((n,1))
    print("This is my x:\n",x)
    x[n-1] = (z[n-1])/(U[n-1,n-1])
    
    for i in range(n-1,-1,-1):
        sum =0
        for j in range(i+1,n):
            sum=sum+((U[i,j])*(x[j]))
        x[i]=(z[i]-sum)/U[i,i]
    return x

##This will computer the least square solution to the algorithm ||Ax(subscript LS)-b||(subscript 2), fully tested
def LeastSquareSolution(A,C):
    (Q,R)= SimpleQRDecomposition(A)
    b =np.matmul(np.transpose(Q),C)
    x= Backward(R,b)    
    return x





##Advance problem sudo code
##This is Algorithm 4, the QR decomposition when columns of A are not linealy independent, not tested 
# def QRNotLinearIndependent(A):
#     (m,n) =np.shape(A)

#     ##Initialize Q and R
#     R= np.zeros((n,n))
#     Q =np.zeros((m,n))
#     rank = 0
#     residual =A[:,0,:1]
#     ##norm_residual = np.linalg.norm(residual)

#     ##row =0

#     for j in range(0,n):
#         if norm_residual <0:  ##This must be changed to a better tolerance, when that is figured out
#             R[row:m,j] = np.zeros((m-row,1)) ## Typo in the sudo code
#         else:
#             R[row,j] =norm_residual
#             Q[:,row] = (residual/norm_residual)
#             rank =rank+1
#             for k in range(j+1,n+1):
#                 R[row,k] =Q[:,row]*A[:,k]
#             if j < n-1:
#                 vector_proj =np.zeros((m,1))
#                 for i in range(1,row+1):
#                     vector_proj = vector_proj+ (R[i,row+1]*Q[:,i])
#                     residual = A[:,j+1]-vector_proj ## This is a colum vector
#             row =row+1
#         norm_residual =np.linalg.norm(residual)


##@param :Will take in a mxn matrix A, not nessasary linearly independent and a tolerance o e which will be a small number
##@return :mxp matrix Q, pxn matrix R, and the rank p of the matrix
def QRImprovedDecomposition(A):
    (m,n) =np.shape(A)

    ##Initialize Q and R and the Rank
    R= np.zeros((n,n))
    Q =np.zeros((m,n))
    rank = 0
    tol=1e-7
    for j in range(0,n):
        vector_proj = np.zeros((m,1))
        for i in range(0,rank):
            ##Vector projection plus the row i in q and r at i,j
            vector_proj =vector_proj+(R[i,j]*Q[:,i:i+1])
        ##The diffrence in our actual A row j and its projection
        residual =A[:,j:j+1] - vector_proj
        norm_residual = np.linalg.norm(residual)
        
        
        ## we will make e the tolerance a very small number
        
        if(norm_residual >= tol):
            rank = rank+1
            R[rank-1,j] =norm_residual
            Q[:,rank-1:rank] = (residual/norm_residual)

            for k in range(j+1,n):
                R[rank-1,k] = np.matmul((np.transpose(Q[:,rank-1:rank])),A[:,k:k+1])
    return Q,R,rank


##Forward substitution algorithm, Tested Workes gets me the correct data for test set
##@param : nxn matric L, rank n, and vector b of nx1
##@return : nx1 vector z that solves Lz =b
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





##Will compute the solution to the least squares proble min ||AxLS-b||
##@param :Takes in matrix mxn A, and vector b of mx1
##@return :x matrix to the LS of QR
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


def main():
    ##test =np.array([[1,2],[1,4],[1,9]])
    ##column =np.matrix([[1],[2],[3]])
    ##Q,R=SimpleQRDecomposition(test)
    ##print("This is the Q for our A QR decomposition:\n",Q)
    ##print("This is the R for our A QR decomposition:\n",R)
    ##x =Backward(test,column)
    ##problemOneA= np.array([[4,0,0,0],[-4,8,-4,2],[-7,7,-3,3],[-2,2,-2,4]])
    ##problemOneX = np.array([[1],[2],[3],[4]])
    ##pONeATranspose =np.matmul(np.transpose(problemOneA),problemOneA)
    ##pONeXTranspose =np.matmul(np.transpose(problemOneA),problemOneX)
    ##solution=LeastSquareSolution(pONeATranspose,pONeXTranspose)
    ##print("This is the solution for the least squares:\n",solution)
    

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
    print("This is a test of my solution y:\n",z)
































    # (Q,R,rank)=QRImprovedDecomposition(test) Tested complete
    # print("This is the Q for our Test QR decomposition Improved:\n",Q)
    # print("This is the R for our Test QR decomposition Improved:\n",R)
    # print("This is the rank for Test: \n",rank)
    # print("This is the Test Matrix:\n",np.matmul(Q,R))
    # print("This is the identiy matrix of Q and R\n",np.matmul(np.transpose(Q),Q))
    
    # L= np.array([[2.,0,0],[1,3,0],[2,3,4]])
    # rank =3
    # b = np.array([[4.],[8],[18]])
    # z =forward(L,rank,b)
    # print("This is my z for test:\n",z)





    
    ##testTranspose=np.matmul(np.transpose(test),test)
    ##columnTranspose=np.matmul(np.transpose(test),column)
    ##solution=LeastSquareSolution(testTranspose,columnTranspose)
    ##print("This is the solution for the least squares:\n",solution)

if __name__ == "__main__":
    main()