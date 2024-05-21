import numpy as np
import matplotlib.pyplot as plt

b2_ps2_Km = 20
b2 = b2_ps2_Km * 1e-27

Lmax = 2000
Npoints = 1000
Rb = 2.5e9

z = np.linspace(0, Lmax, Npoints) * 1e3 
T0 = 1 / Rb

Tz = T0 * np.sqrt(1 + (b2 * z / T0**2) ** 2 )

BF = Tz / T0
plt.close('all')
plt.plot(z/1e3, BF)
plt.xlabel('z [Km]')
plt.ylabel('BF')




 
 