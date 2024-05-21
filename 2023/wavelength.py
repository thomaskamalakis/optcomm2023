f = 2.4e9
c = 3e8
l = c/f
print('f=', f, 'Hz, l = ',l,'m')

f = 60e9
l = c/f
print('f=', f, 'Hz, l = ',l,'m')

f = 400e12
l = c/f
print('f=', f, 'Hz, l = ',l,'m')

f0 = 200e12
l0 = c/f0
print('f0=', f0, 'Hz, l0 = ',l0,'m')

Dl = 200e-9

l1 = l0 - Dl/2
l2 = l0 + Dl/2

f1 = c / l1
f2 = c / l2
Df = f1 - f2
print('Df = ', Df/1e12)