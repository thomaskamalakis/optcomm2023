import numpy as np
import matplotlib.pyplot as plt

def calc_dB(A):
    return 10 * np.log10(A)

def calc_dBm(P):
    return 10 * np.log10(P / 1e-3)

def invcalc_dB(AdB):
    return 10 ** (AdB/10)

def invcalc_dBm(PdBm):
    return 1e-3 * 10 ** (PdBm/10)
    
L = 100
print('L[dB]=', calc_dB(L),'dB' )

L = 0.0001
print('L[dB]=', calc_dB(L),'dB' )

P = 1
print('P[dBm]=', calc_dBm(P),'dBm' )

P = 1e-6
print('P[dBm]=', calc_dBm(P),'dBm' )

LdB = -25
print('L=', invcalc_dB(LdB) )

PdBm = 0
print('P=', invcalc_dBm(PdBm) )

a = 0.01
l = 100

L = np.exp(-a * l)
print('L=',L, 'L[dB]=', calc_dB(L),'dB' )

l = np.linspace(0, 1000, 20)
L = np.exp(-a * l)
plt.close('all')
plt.figure()
plt.plot(l, L)

plt.figure()
plt.plot(l, calc_dB(L))

adB = 10 * np.log10( np.exp(1) ) * a
plt.plot(l, -adB * l, 'o')

adB = 0.25
l0 = 100
LdB = -adB * l0
print('L[dB]=', LdB,'dB' )
print('L=',invcalc_dB(LdB))

l1 = 50
L1dB = - adB * l1

GdB = 20

l2 = 50
L2dB = - adB * l2

LdB = L1dB + GdB + L2dB
print('L[dB]=', LdB,'dB' )
print('L=',invcalc_dB(LdB))








 