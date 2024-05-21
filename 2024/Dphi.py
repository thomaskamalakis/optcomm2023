import numpy as np
import matplotlib.pyplot as plt

Dphi = np.linspace(0, 4 * np.pi, 200)
x = 1 + np.exp(1j*Dphi)
P = np.abs(x) ** 2

plt.close('all')
plt.figure()
plt.plot(Dphi, P)
plt.xlabel('Dphi')
plt.ylabel('P')

L1 = 10e-6
L2 = 20e-6
n = 1.5
l = np.linspace(1.3e-6, 1.8e-6, 1000)
Dphi = 2 * np.pi * n / l * (L2-L1)
x = 1 + np.exp(1j*Dphi)
P = np.abs(x) ** 2

plt.figure()
plt.plot(l, P)
plt.xlabel('l ')
plt.ylabel('P')
