
import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(0.0, 20.0, 100)
w = 1e-9  # width of quantum well in nm
V = 20    # volts in ev
Tolerance = 1e-3


#Constants
MassOfElectron=9.1094e-31

ElectronVolt=1.602e-19

h_bar=1.0545e-34
#numerator/Denom
Top = ((w ** 2)*((MassOfElectron)))/ElectronVolt
Bottom=(2*((h_bar/ElectronVolt)**2))
Values=Top/Bottom

#Functions

def Tan(Energy):  
    return np.tan(np.sqrt(Values * Energy))


def Even(Energy): 
    return np.sqrt((V - Energy) / Energy)


def Odd(Energy): 
    return (-np.sqrt(Energy / (V - Energy)))



#plotting functions
y1 = Tan(E)
y2 = Even(E)
y3 = Odd(E)
plt.plot(E,y1, label='Tan')
plt.plot( E,y2, label='Even')
plt.plot(E,y3,label='Odd')
plt.legend()
plt.title("Functions")
plt.show()

#Bisection 
def TanOfEven(x):
    return Tan(x) - Even(x)


def TanOfOdd(x):
    return Tan(x) - Odd(x)


def crit(f, x1, x2, Tolerance):

    def midpoint(x, y):
        return (x + y) / 2

    def sign(x, y):
        if (x < 0 and y < 0) or (x > 0 and y > 0):
            return True
        else:
            return False
        
    while abs(x1 - x2) > Tolerance:
        x = midpoint(x1, x2)
        if sign(f(x1), f(x)):
            x1 = x
        elif sign(f(x), f(x2)):
            x2 = x
        elif abs(x) < Tolerance:
            return x
    
    return midpoint(x1, x2)

print('Test between points 1 & 5= ', crit(TanOfEven, 1, 5, Tolerance))

print('3 to 5', crit(TanOfEven, 3, 5, Tolerance))
print('9 to 12', crit(TanOfEven, 9, 12, Tolerance))
print('13 to 17', crit(TanOfEven, 13, 17, Tolerance))
print( '18 to 20', crit(TanOfEven, 18, 20, Tolerance))