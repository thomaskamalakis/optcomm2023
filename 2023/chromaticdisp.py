import numpy as np
import matplotlib.pyplot as plt

b2 = 20e-27
Rb = 100e9
T0 = 1 / Rb
L = np.linspace(1e3, 100e3, 100)
BF = np.sqrt(1 + (b2 * L / T0 ** 2)  ** 2)
plt.close('all')
plt.figure()
plt.plot(L/1e3, BF)
plt.xlabel('L [Km]')
plt.ylabel('BF')

Rb = np.linspace(10e9, 100e9, 100)
LD = 1 / b2/ Rb ** 2
plt.figure()
plt.loglog(Rb/1e9, LD/1e3)
plt.xlabel('Rb [Gb/s]')
plt.ylabel('LD [Km]')
