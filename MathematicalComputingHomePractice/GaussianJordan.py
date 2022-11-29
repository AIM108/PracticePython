import numpy as np
import copy




##Gaussian Elimination Algorithm, couldn't get it to work
def geaNotes(matrixA):
    (m,n)=np.shape(matrixA)
    for i in range(0,m-1):
        print("Current row:",i)
        j =p+1
        flag=0
        while j<=n and flag ==0:
            print("currrent colum:",j)
            ##Implmentaion migth not be right
            print("looking a values:",matrixA[i:,j])
            imax=np.argmax(matrixA[i:,j])
            print("Row imax:",imax)
            ##Check code above
            if (matrixA[imax,j]==0):
                j=j+1
            else:
                p=j
                flag=1
                ##swap row i with row imax
                rowA=copy.deepcopy(matrixA[imax,:]) 
                print("i max row:",rowA)
                rowB= copy.deepcopy(matrixA[i,:])
                print("current row:",rowB)
                matrixA[i,:]=copy.deepcopy(rowA)
                matrixA[imax,:]=copy.deepcopy(rowB)
                print("new matrixA:\n",matrixA)

                ##Make the pivot element 1
                rowC= copy.deepcopy((1/(matrixA[i,p]))*matrixA[i,:])
                print("New row reduced pivot to one:",rowC)
                matrixA[i,:]=copy.deepcopy(rowC)

                ##Make all numbers under i on j equal to zero
                for h in range((i+1),m):
                    matrixA[h,:]=copy.deepcopy(((-matrixA[h,p])*matrixA[i,:])+(matrixA[h,:]))

                print("new matrixA:\n",matrixA)


##MyVersion, I couldn't get the sudo code to work properly
def gea(matrixA):
    (m,n)=np.shape(matrixA)
    x=0
    for i in range(0,m-1):
        print("Current row:",i)
        
        
        print("currrent colum:",x)
        maxRowIndex=np.argmax(matrixA[i:,x])
        maxRowIndex=(x*1)+maxRowIndex
        print("Looking at this matrix to find maxRowIndex:\n",matrixA[i:,x])
        print("maxRowIndex:",maxRowIndex)
        if(matrixA[maxRowIndex,x]==0):
            print("do nothing")
        else:
            ##swap row i with row imax
            maxRow=copy.deepcopy(matrixA[maxRowIndex,:]) 
            currentRow= copy.deepcopy(matrixA[i,:])
            matrixA[i,:]=copy.deepcopy(maxRow)
            matrixA[maxRowIndex,:]=copy.deepcopy(currentRow)
            print("new switch matrixA:\n",matrixA)

            ##Make the pivot element 1
            reducedCurrentRow= copy.deepcopy((1/(matrixA[i,x]))*matrixA[i,:])
            matrixA[i,:]=copy.deepcopy(reducedCurrentRow)

            ##Make all numbers under i on j equal to zero
            for h in range((i+1),m):
                matrixA[h,:]=copy.deepcopy(((-matrixA[h,x])*matrixA[i,:])+(matrixA[h,:]))
            print("Reduced Matrix:\n",matrixA)
        x=x+1
    print("Final matrixA:\n",matrixA)


            

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
    A=np.matrix([[1.,1.,-1],[2,0,1],[-1,0,2]])
    ##gaussJordanReduction(A)
    print("Starting matrix:\n",A)
    gea(A)
 



def main():
    ##gJTest()
    print (5-(-2))


if __name__ =="__main__":
    main()