import numpy as np

##Gauss-Jordan Algorithm
def gaussJordanReduction(matrixA):
    (m,n)=np.shape(matrixA)
    print(m,n)
    for i in range(m-1,1,-1):
        print(i)
        j=1
        flag=0
        while (flag ==0) and (j<n):
            if(matrixA[i,j]==0):
                j=j+1
            else:
                flag=1
        if (flag ==1):
            q=i-1
            for k in range(q,1,-1):
                rowK =np.reshape(matrixA[k,:],(1,len(matrixA[1,:])))
                print(rowK)
                rowI =np.reshape(matrixA[i,:],(1,len(matrixA[1,:])))
                print(rowI)
                matrixA[k,:]=((-matrixA[k,j])*rowI)+rowK
                print(k)

def gJTest():
    A=np.matrix([[1,2,-1,4],[0,1,0,3],[0,0,1,2]])
    gaussJordanReduction(A)
def main():
    gJTest()

if __name__ =="__main__":
    main()