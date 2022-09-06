import numpy as np
import matplotlib.pyplot as plt


t=[0.5,3,7,11,15];
T=[85,48,35,33,31];

A=30;
B=40;

m=-0.276;

templist=[];

for x in t:
   
   temp=float(A)+(float(B)**(m*np.float_(x)));
   print(temp);