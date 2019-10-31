# Excercise 4.4
#finding an integral
#y_k = \sqrt{1-x_k^2} and x_k = -1 + hk.
#I = \lim_{N\to\infty} \sum_{k=1}^N hy_k 

import math
import matplotlib.pyplot as plt
import numpy as np
import time
import timeit
from functools import partial



n=100

def integral(n):
    answer=0
    h=2/n
    
    for k in range (1, n+1):
    
        xk= -1 +h* k 
        yk= np.sqrt(1-xk**2)
        answer += h*yk
    return answer
t= (timeit.timeit(partial(integral, n), number=1))
print('The integral calculated within {:.4f} seconds given {} slices is {}' .format(t,n,integral(n)))





n2=400000

def integral2(n2):
    answer2=0
    h=2/n2
    
    for k in range (1, n2+1):
    
        xk= -1 +h* k 
        yk= np.sqrt(1-xk**2)
        answer2 += h*yk
    return answer2

t2= (timeit.timeit(partial(integral2, n2), number=1))

print('The integral calculated within {:.2f} seconds given {} slices is {} and thefore has improved with added time and slices'.format(t2,n2,integral2(n2)))

