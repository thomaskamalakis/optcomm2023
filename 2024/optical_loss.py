#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:49:01 2024

@author: thkam
"""

import numpy as np
import matplotlib.pyplot as plt

def to_W(P):
    return 1e-3 * 10 ** (P/10)

adB = 0.25
L = np.arange(0, 2, 0.001)   # Km
PT = 10                 # dBm
PR = PT - adB * L       # Receiver power [dBm]

plt.close('all')
plt.figure()
plt.plot(L, PR)
plt.xlabel('L [Km]')
plt.ylabel('PR [dBm]')

PR_W = to_W(PR)
plt.figure(2)
plt.plot(L, PR_W/1e-3)
plt.xlabel('L [Km]')
plt.ylabel('PR [mW]')

