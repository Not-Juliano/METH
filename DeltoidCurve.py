
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace

theta =np.linspace( 0,2*np.pi)
x= 2*np.cos(theta) + np.cos(2*theta)
y= 2*np.sin(theta) - np.sin(2*theta)





phi =np.linspace(0,10*np.pi, num= 200)

def f(phi):
    return phi**2


r= f(phi)
x1 =r*np.cos(phi) 
y1 =r*np.sin(phi) 






import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace




Phi =np.linspace(0,24*np.pi, num = 2000)


r=np.exp(np.cos(Phi) - 2*np.cos(4*Phi) +( np.sin(Phi/12)**5))

x2=r*np.cos(Phi) 
y2=r*np.sin(Phi) 



plt.figure(figsize=(15,5))
plt.subplot (1,3,1)
plt.plot (x,y,'m^',label='Featuring: Cool Triangles')
plt.title('Deltoid Curve')
plt.legend()



plt.subplot (1,3,2)
plt.plot (x1,y1,'ro',label='Hypnosis')
plt.title('Galilean Spiral')
plt.legend()

plt.subplot (1,3,3)
plt.plot(x2,y2,'b*', label='Schwifty Stars')
plt.title('Fey’s Function')
plt.legend()

plt.show()