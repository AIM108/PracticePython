
##Question Two

import numpy as np
import matplotlib.pyplot as plt

t=[0.5,3,7,11,15];
T=[85,48,35,33,31];

A=30;
B=40;
m=-0.276;


tempValue=A+B**(m*np.float_(t));
print(tempValue);


plt.xlabel("Time");
plt.ylabel("Temperature");
plt.title("Time x Temperature using equation A+B^(m*t)");
plt.plot(tempValue,T);
plt.show();
