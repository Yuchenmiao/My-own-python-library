from scipy.fftpack import fft,fftshift
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

# Load signals
signal = loadmat('C:/Users/18063/Desktop/SI100/SI100B_SP_HW1/signal/q3/q3_signal1.mat')
data = signal['signal1']
data = data[0]


# Create the Butterworth filter with Wn = 10 Hz
from scipy import signal
fs = len(data)
b, a = signal.butter(10, 10, 'lowpass', fs=fs)

# Apply the highpass filter to get the clean noise
filtered_signal = signal.filtfilt(b, a, data)

# Plot the filtered signals
time_coord = np.arange(0, 1, 1/200)
plt.plot(time_coord, filtered_signal)
plt.xlabel=('Time (s)')
plt.ylabel=('Amplitude')
plt.tight_layout(pad = 1.0) # for better spacing
plt.show()