import numpy as np



""""
##Python works in default with list
A=[1,2,3,4];
print("The variable A is of type: ",type(A));

##Using numpy we are able to create objects of type numpy.ndarray which are treated as matrices
A=np.array([[1,2,3,4]]);
print("Using the libary numpy we are able to assign our variable A an object of type: ",type(A));
print("Matrix A:\n",A);

##In python only matrices with one row can be transposed, n=1 then nxm is true but if n>1 then you can not use T transpose
u=A.T;
print("Matix u: \n",u);

print("\n The matrix u is tylpe: ",type(u));

"""
"""""
##Multiplication in Python works nxm multiply axb  m=a, we use the function matmul(arrayA,arrayB)
A=np.array([[81,98,53.],[1,9,7.]]);
B=np.array([[1.],[2],[4]]);
C=np.matmul(A,B);
print("The multiplication of A and B matrices is C: \n",C);
print("\nIt is of type: ",type(C));

##Copying a single element of a array
D=A[0,0].copy();
E=A[0,0];
print("The object D is a copy of the A[0,0] of the array A: ",D," and is of type: ",type(D)," and at location: ",id(D),"\n");
print("The object E is a shallow copy of A[0,0] of the array A: ",E," and is of type: ",type(E)," and at location: ",id(E),"\n");
print("The orignal location of A[0,0] is: ",id(A[0,0])," and its value is: ",A[0,0]);
print(A);
##Shallo copy
z=A;
y=z;
print(A);
print(y);
print(z);
A[0,0]=200;

print(A);
print(y);
print(z);

"""
"""""
##Copying an whole row in python

A=np.array([[1,2,3],[3,2,1]]);
print(A);
R1=A[0,:].copy();
R2=A[1,:].copy();
print("R1 is a copy of the row A[0] ", R1, " and is of type single list",type(R1),"\n");
print("R1 is a copy of the row A[0] ", R2, " and is of type single list",type(R2),"\n");

R3=np.reshape(A[0,:],(1,3));
R4=np.reshape(A[1,:],(1,len(A[0,:])));
print(R3);
print(R4);

print("Printing the last element of the array at row 0 : ",A[0,-1]);

##To find a entries that equal to x, it will return the location where the argument is true
I=np.argwhere(A==3);
print(A);
print(I);
J=np.argwhere(A==200);
print(J);

print(A[I[0,0],I[0,1]]);
print(I[0,0],I[0,1]);

"""""

"""""
A = np.array([[1.,2,3] , [ 4 , 5 , 6 ] ] )

J=np.argwhere(A>=5.);
print(J);

print("\n",A[J[0],J[1]]);
c=A[J[0],J[1]];
C=np.reshape(c,(len(c),1));
print(C);
"""


A=np.array([[1,2,2,3],[43.,36,0,9]]);
print(A);

I= np.argwhere(A==1);
A=np.delete(A,I[0]);
A=np.append(A,9.0);
A=np.reshape(A,(2,4));
print(A);

C=np.array([[1.,2,3],[6,7,8]]);
B=np.array([[4.,5],[9,10]]);

D=np.array([[11.,12,13,14,15]]);

C=np.concatenate((C,B), axis=1); ##Columns
C=np.concatenate((C,D), axis=0); ##rows

print(C);





