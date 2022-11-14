import numpy as np




##Gaussian Elimination Algorithm
def gea(matrixA):
    (m,n)=np.shape(matrixA)
    p=0
    for i in range(0,m-1):
        j =p+1
        flag=0
        while j<=n and flag ==0:
            ##Implmentaion migth not be right
            imax=(np.argmax(matrixA[i:,j]))*abs(matrixA[(np.argmax(matrixA[i:,j])),j])
            print(np.argmax(matrixA[i:,j]))
            print(imax)
            ##Check code above
            flag=1

            

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
                rowK =matrixA[k,:]
                print(rowK)
                rowI =matrixA[i,:]
                print(rowI)
                matrixA[k,:]=((-matrixA[k,j])*rowI)+rowK
                print(k)

def gJTest():
    A=np.matrix([[1,1,-1],[2,-1,1],[-1,2,2]])
    ##gaussJordanReduction(A)
    gea(A)
 



def main():
    gJTest()

if __name__ =="__main__":
    main()