import numpy as np
import matplotlib.pyplot as plt

B = np.linspace(10e6, 1e9, 100)
n1 = 1.5
n2 = 1.495
c = 3e8

D = (n1 - n2) / n1
L = 0.5 * n2 * c / n1 ** 2 / D / B

plt.close('all')
plt.figure()
plt.loglog(B / 1e6, L)
plt.ylabel('L [m]')
plt.xlabel('B [Mb/s]')
plt.grid()