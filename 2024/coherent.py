#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

phi1 = np.pi
phi2 = np.linspace(0, 2*np.pi, 1000)

x = np.exp(1j*phi1) + np.exp(1j*phi2)
plt.close('all')
plt.plot(phi2-phi1, np.abs(x) ** 2)