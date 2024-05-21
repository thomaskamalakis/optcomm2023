#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:49:01 2024

@author: thkam
"""

c = 3e8
Dl = 35e-9
l0 = 1550e-9
nse = 0.4

Df = c / l0 ** 2 *Dl
print('Df = ', Df / 1e12, 'THz' )

Rb = nse * Df
print('Rb = ', Rb/1e12, 'Tb/s')