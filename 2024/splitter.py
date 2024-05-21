import numpy as np
import matplotlib.pyplot as plt

def Lsplitter(N):
    return 10 * np.log10(N)

def Lfiber(L, adB = 0.2):
    return adB * L

Rb_tot = 10
L_pol = 0.5
L_extra = 2
L_bal = 2
L_splice = 0.3

L_tot = L_pol + L_extra + L_bal + 4 * L_splice

PT = np.linspace(10, -10, 100)
PR_min = -30.0
L1 = 5.0
L2 = 1.0

Lfib = Lfiber(L1+L2)

N = 10.0 ** ( (PT-PR_min - Lfib ) / 10 )
N2 = 10.0 ** ( (PT-PR_min - Lfib - L_tot ) / 10 )

plt.close('all')
plt.figure()
plt.plot(PT, N, label='ideal')
plt.plot(PT, N2, label='extra losses')

plt.xlabel('PT [dBm]')
plt.ylabel('N')
plt.legend()

plt.figure()
plt.plot(N, Rb_tot/N)

plt.ylabel('Rb [Gb/s]')
plt.xlabel('N')

