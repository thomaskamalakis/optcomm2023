c = 3e8
l0 = 1550e-9
Dl = 100e-9

l1 = l0 - Dl / 2
l2 = l0 + Dl / 2
Df = c / l1 - c/ l2
print('Df = ', Df/1e12, 'THz')

Df2 = c / l0 ** 2 * Dl
print('Df2 = ', Df2/1e12, 'THz')

print( l0**2 / (Dl**2 / 4) )

A = c / l0 ** 2
print('A=', A)

e = 0.4
Rb = e * Df
print('Rb=', Rb / 1e12, 'Tb/s')

Rb_channel = 40e9
Df_channel = Rb_channel / e
print('Df_channel=', Df_channel / 1e9, 'GHz')

Nch = Df / Df_channel
print('Nch = ', Nch)
