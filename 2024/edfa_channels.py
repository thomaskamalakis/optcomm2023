import numpy as np

Df_demux = 100e9
Df_p = 25e9

c = 3e8
sp_ef = 0.4

l1 = 1530e-9
l2 = 1565e-9
Dl = l2 - l1

f1 = c/l1
f2 = c/l2

Df = f1-f2
print('Df =',Df/1e12,'THz')

Rb = sp_ef * Df
print('Rb =',Rb/1e12,'Tb/s')

Nch = np.floor(Df / Df_demux)
print('Nch = ',Nch)

Rb_ch = Df_p * sp_ef
print('Rbch = ',Rb_ch/1e9, 'Gb/s')

Rb_edfa = Rb_ch * Nch
print('Rb_edfa = ',Rb_edfa/1e12, 'Tb/s')


 