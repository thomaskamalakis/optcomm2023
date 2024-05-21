import numpy as np
import matplotlib.pyplot as plt

b2_ps2_Km = 20
b2 = b2_ps2_Km * 1e-27

Rb = np.linspace(2.5e9, 100e9, 1000)
T0 = 1/Rb
LD = T0 ** 2 / np.abs(b2)
 
plt.close('all')
plt.semilogy(Rb/1e9, LD/1e3)
plt.xlabel('Rb [Gb/s]')
plt.ylabel('LD [Km]')




 
 