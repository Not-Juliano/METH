import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
N=1000


values= np.zeros([N,N])

Possible_Steps=['up','down','right', 'left']

path=[]
walk=[]

The_Drunk=np.array([0,0])


random.seed(1)

  #for amount of steps(N), either +/- 1 to I or J, but <x or y edge
   #else choose another direction
   # and keep track so I know it's path 
for i in range (N):
    motion=random.choice(Possible_Steps)
    path.append(motion)



for i in path:
    walk.append(np.copy(The_Drunk)) 
    #print(The_Drunk)
    #print(i)   
    if i == 'up':
        The_Drunk[0]+=1
        
    if i == 'down':
        The_Drunk[0]-=1
        
    if i == 'left':
        The_Drunk[1]-=1
        
    if i =='right':
        The_Drunk[1]+=1  


walk = np.transpose(np.array(walk))
#rint('the walk in an array:',walk)
print('x positions', walk[0])
print('y positions', walk[1])




fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
Drunk = plt.Circle((0, 0), radius=1, fc='r')

def init():
    Drunk.center = (0, 0)
    ax.add_patch(Drunk)
    return Drunk,

def animate(i):
    x=walk[0]
    y=walk[1]
    Drunk.center = (x[i], y[i])
    return Drunk,



anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=361,interval=20,blit=True)
anim.save('drunk3.mp4')