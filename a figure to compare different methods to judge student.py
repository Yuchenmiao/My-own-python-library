import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 1000)
y1 = x
y2 = np.sqrt(x) * 10

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y2 - y1)

plt.show()