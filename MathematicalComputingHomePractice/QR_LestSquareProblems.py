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


##This is Algorithm 4, the QR decomposition when columns of A are not linealy independent, not tested 
def QRNotLinearIndependent(A):
    (m,n) =np.shape(A)

    ##Initialize Q and R
    R= np.zeros((n,n))
    Q =np.zeros((m,n))
    residual =A[:,0,:1]
    norm_residual = np.linalg.norm(residual)

    row =0
    rank =0

    for j in range(0,n):
        if norm_residual <0:  ##This must be changed to a better tolerance, when that is figured out
            R[row:m,j] = np.zeros((m-row,1)) ## Typo in the sudo code
        else:
            R[row,j] =norm_residual
            Q[:,row] = (residual/norm_residual)
            rank =rank+1
            for k in range(j+1,n+1):
                R[row,k] =Q[:,row]*A[:,k]
            if j < n-1:
                vector_proj =np.zeros((m,1))
                for i in range(1,row+1):
                    vector_proj = vector_proj+ (R[i,row+1]*Q[:,i])
                    residual = A[:,j+1]-vector_proj ## This is a colum vector
            row =row+1
        norm_residual =np.linalg.norm(residual)





def main():
    ##test =np.array([[1,2],[1,4],[1,9]])
    ##column =np.matrix([[1],[2],[3]])
    ##Q,R=SimpleQRDecomposition(test)
    ##print("This is the Q for our A QR decomposition:\n",Q)
    ##print("This is the R for our A QR decomposition:\n",R)
    ##x =Backward(test,column)
    problemOneA= np.array([[4,0,0,0],[-4,8,-4,2],[-7,7,-3,3],[-2,2,-2,4]])
    problemOneX = np.array([[1],[2],[3],[4]])
    pONeATranspose =np.matmul(np.transpose(problemOneA),problemOneA)
    pONeXTranspose =np.matmul(np.transpose(problemOneA),problemOneX)
    solution=LeastSquareSolution(pONeATranspose,pONeXTranspose)
    print("This is the solution for the least squares:\n",solution)
    
    
    ##testTranspose=np.matmul(np.transpose(test),test)
    ##columnTranspose=np.matmul(np.transpose(test),column)
    ##solution=LeastSquareSolution(testTranspose,columnTranspose)
    ##print("This is the solution for the least squares:\n",solution)

if __name__ == "__main__":
    main()