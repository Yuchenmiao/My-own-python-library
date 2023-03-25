from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

signal = loadmat('C:/Users/18063/Desktop/SI100/SI100B_SP_HW1/signal/q2/q2_signal.mat')
data = signal['data']
data = data[0]
time_coord = np.arange(0, 0.0012, 0.0012/600)
plt.plot(time_coord, data)
plt.xlabel('Time (s)')
plt.ylabel('Signal (V)')
plt.title('Signal in time domain')
plt.show()