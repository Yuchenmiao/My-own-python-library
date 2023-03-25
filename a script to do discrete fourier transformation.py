from scipy.fftpack import fft,fftshift
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

signal = loadmat('C:/Users/18063/Desktop/SI100/SI100B_SP_HW1/signal/q2/q2_signal.mat')
data = signal['data']
data = data[0]

fs = len(data)
N = 1024
z = fft(data,N)
z = fftshift(abs(z))
axis_freq = np.arange(-N/2,N/2)*fs/N
amp_freq = np.abs(z)/len(data)*2
plt.plot(axis_freq,amp_freq)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.title('Signal in frequency domain')
plt.show()