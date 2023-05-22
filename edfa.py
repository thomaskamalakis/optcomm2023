import numpy as np
import matplotlib.pyplot as plt

c = 3e8
l0 = 1550e-9
Dl = 100e-9
Rb = 40e9
e = 0.4
Df_ch = Rb / e

lmin = l0 - Dl / 2
lmax = l0 + Dl / 2

fmin = c / lmax
fmax = c / lmin

print('fmin = %6.2fTHz fmax = %6.2fTHz ' %(fmin/1e12, fmax/1e12))

Df_fiber = fmax - fmin
print('Df_fiber = %6.2fTHz ' % (Df_fiber/1e12) )
print('Df_ch = %6.2fGHz ' % (Df_ch/1e9) )

Nch_fiber = np.floor(Df_fiber / Df_ch)
print('Nch_fiber = %6.2f ' % Nch_fiber )

print('--------------------------')
print('          EDFA')
print('--------------------------')

lmin = 1530e-9
lmax = 1565e-9

fmin = c / lmax
fmax = c / lmin

print('fmin = %6.2fTHz fmax = %6.2fTHz ' %(fmin/1e12, fmax/1e12))

Df_edfa = fmax - fmin
print('Df_edfa = %6.2fTHz ' % (Df_edfa/1e12) )
print('Df_ch = %6.2fGHz ' % (Df_ch/1e9) )

Nch_edfa = np.floor(Df_edfa / Df_ch)
print('Nch_edfa = %6.2f ' % Nch_edfa )







 
