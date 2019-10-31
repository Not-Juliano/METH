

#imports

import astropy.constants as c
import astropy.units as u
import numpy as np
from numpy import linspace
import mpmath



#labeling constants
a=1e-8 #getting very close to zero
b=(np.pi)/2
n=1000
k=1
s=0
h=(b-a)/n
w= (c.k_B)**4/(4*np.pi**2*(c.c)**2*(c.hbar)**3)


#here we use the tan transformation and create a function that uses it.

def fun(x):
    z=np.tan(x)
    function=((z**3)*mpmath.sec(x)**2)/((np.exp(z)-1))
    return function

#Create a loop, and the fundamentals of the trapezodial method 

for k in range(1, n):
    s+=fun(a+k*h)
    
final=h*(0.5*fun(a)+0.5*fun(b)+s)

final*w



output=final*w

print(type(float(output.value)))

print( " The Stefan Boltmann Constant is {:.2e}{}".format(float(output.value),output.unit))





