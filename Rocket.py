

# A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. 
# Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, 
# then print out the time in years that the spaceship takes to reach its destination 
# (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship.
#  Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.


import astropy.constants as c
import astropy.units as u
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt
import mpmath
import math


c = 3e8
velocity = float(input("Enter velocity as a fraction of the speed of light, eg 0.5):  "))
if velocity > 1:
     print('Number must be a fraction of the speed of light.')
     exit(0)

distance = float(input('What is the distance away, in terms of light years?'))


tE = distance/velocity


gamma= 1/(np.sqrt(1-velocity**2))
newx= distance/gamma

tS= newx/velocity


text ='The time taken in Earths reference frame  is {:.2f} years, while the time in the Spaceships reference frame is {:.2f} years '.format((tE), (tS))

print(text)

