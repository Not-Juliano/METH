#!/usr/bin/env python
# coding: utf-8

# Deltoid curves

# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace

theta =np.linspace( 0,2*np.pi)
x= 2*np.cos(theta) + np.cos(2*theta)
y= 2*np.sin(theta) - np.sin(2*theta)


plt.plot(x,y)
plt.show()


# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace


def f(θ):
    return θ**2
r= f(θ)


θ =np.linspace(0,10*np.pi, num= 200)

x1 =r*np.cos(θ) 
y1 =r*np.sin(θ) 




plt.plot(x1,y1)
plt.show()


# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace




θ =np.linspace(0,24*np.pi, num = 2000)


r=np.exp(np.cos(θ) - 2*np.cos(4*θ) +( np.sin(θ/12)**5))

x2=r*np.cos(θ) 
y2=r*np.sin(θ) 




plt.plot(x2,y2)
plt.show()


# In[ ]:


plt.figure(figsize=(15,5))
plt.subplot (1,3,1)
plt.plot (x,y,'m^')

plt.subplot (1,3,2)
plt.plot (x1,y1,'ro')

plt.subplot (1,3,3)
plt.plot(x2,y2,'b*')


# In[ ]:




