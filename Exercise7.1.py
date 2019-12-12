#7.1
#Write Python programs to calculate the
#  coefficients in the discrete 
# Fourier transforms of the following periodic functions
#  sampled at N = 1000 evenly spaced points, and make
#  plots of their amplitudes:
import numpy as np
import matplotlib.pyplot as plt

#Square wave
N=1000
Amp=1
#set the last 50% of the array to zero
Squaredata= np.arange(0,N)
Squaredata[0:500]=1
Squaredata[500:N]=-1



#take a real fourier transform of this data
fftSquaredata=np.fft.rfft(Squaredata)
Squared_data=fftSquaredata*np.conjugate(fftSquaredata)




#for sawtooth
from scipy import signal


s= np.linspace(0,1,1000)
sawtooth=(signal.sawtooth(s*6*np.pi))
plt.plot(s,sawtooth)
fftSawtooth=np.fft.rfft(sawtooth)
sawtooth_data=fftSawtooth*np.conjugate(fftSawtooth)



#for The modulated sine wave yn = sin(πn/N) sin(20πn/N) 
sinn=np.arange(0,1000,1)
y=np.sin(np.pi*sinn/1000)*np.sin(20*np.pi*sinn/1000)
fftsinwave=np.fft.rfft(y)
sinwavedata=fftsinwave*np.conjugate(fftsinwave)

plt.plot(sawtooth)
plt.title('Sawtooth wave')
plt.show()
plt.plot(sawtooth_data)
plt.title('FFT of Sawtooth')
plt.show()

plt.plot(y)
plt.title('SinWave')
plt.show()
plt.plot(sinwavedata)
plt.title('FFT sinwave')
plt.show()



plt.plot(Squaredata)
plt.title('SquareWave')
plt.show()
plt.plot(Squared_data)
plt.title('FFT of Square Wave')
plt.show()