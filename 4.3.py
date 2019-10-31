import math
import matplotlib.pyplot as plt
import numpy as np
import time
import timeit
from functools import partial


#Exercise 4.3: Calculating derivatives
def f(x): #defining the function
    function= x*(x-1)
    return function

delta= 1e-2   #1x10^-2
x=1       # at the point x =1


dfdx= (f(x+delta)-f(x) )/ (delta)    #making use of the function and using deltas.
print ('In the function x(x-1) where delta is 1x10^-2, and x=1, dfdx is {:.2f}'.format (dfdx))



deltas= np.array([1e-4, 1e-6,  1e-8,1e-10,  1e-12 , 1e-14])
dfdx1= (f(x+deltas)-f(x) )/ (deltas) #we calculate all the values in the above array 'deltas'


plt.plot (np.log10(deltas), dfdx1, 'mo') #log10 because the graph takes really small values otherwise.
plt.title('An array of deltas by dfdx')
plt.show()