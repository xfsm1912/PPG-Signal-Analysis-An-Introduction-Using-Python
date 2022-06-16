import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)

y = np.sin(t)

# generate a square wave
# y = np.sin(t) + (1/3) * np.sin(3*t)
y = np.sin(t) + (1/3) * np.sin(3*t) + (1/5) * np.sin(5*t)

plt.plot(y)
plt.show()
