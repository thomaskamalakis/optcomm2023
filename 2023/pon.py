import numpy as np
import matplotlib.pyplot as plt

a = 0.2
l = 3
l_dash = 1
L_splice = 0.5
L_insertion = 2
L_uniform = 2
L_pol = 0.5
P_S = -35

n = np.arange(2, 12)
N = 2 ** n

LS = 10 * np.log10(N) + L_insertion + L_uniform + L_pol
plt.close('all')
plt.plot(N, LS, '-o')
plt.xlabel('N')
plt.ylabel('LS [dB]')

Ltot = LS + a*l + a*l_dash + 4 * L_splice 
plt.figure()
plt.plot(N, LS, '-o', label = 'splitter')
plt.plot(N, Ltot, '-o', label = 'total')

plt.xlabel('N')
plt.ylabel('L [dB]')
plt.legend()

PT = P_S + Ltot
plt.figure()
plt.plot(N, PT, '-o', label = 'PT')

plt.xlabel('N')
plt.ylabel('PT [dBm]')
plt.legend()
