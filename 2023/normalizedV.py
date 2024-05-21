import numpy as np
import matplotlib.pyplot as plt

n1 = 1.5
n2 = np.linspace(1.48, 1.495, 100)
N = n2.size
a = 4e-6
l = 2e-6

V = 2 * np.pi * a / l * np.sqrt(n1 ** 2 - n2 ** 2)
D = 100 * (n1 - n2) / n1
plt.close('all')
plt.figure()
plt.plot(D, V)
plt.xlabel('D [%]')
plt.ylabel('V')
plt.plot(D, 2.405 * np.ones(N), 'r--' )