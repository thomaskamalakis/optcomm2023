import numpy as np
import matplotlib.pyplot as plt

def mybox(x):
    return x - 0.1 * x ** 2 
x = np.linspace(0, 3, 100)
y = mybox(x)

plt.close('all')
plt.figure()
plt.plot(x, y)

f1 = 1
f2 = 2

t = np.linspace(0, 10, 1000)
x1 = 5 * np.sin(2 * np.pi * f1 * t)
y1 = mybox(x1)

plt.figure()
plt.plot(t, x1, label = 'x1')
plt.plot(t, y1, label = 'y1')
plt.legend()

 
