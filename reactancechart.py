# -*- coding: utf-8 -*-
"""
@author: Falk Kyburz
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Limits for impedances
freq_min_pow = 1
freq_max_pow = 9
imp_min_pow = -3
imp_max_pow = 7

# Create figure
fig, ax1 = plt.subplots()

# Create a loglog plot in axes 1
ax1.loglog()

# Plot the loglog grid
for x in range(freq_min_pow, freq_max_pow):
    for y in range(1, 10):
        if y == 1:
            ax1.axvline(y*10**x, ymin=0, ymax=1, linewidth=1, color='r')
        else:
            ax1.axvline(y*10**x, ymin=0, ymax=1, linewidth=0.5, color='r')

for x in range(imp_min_pow, imp_max_pow):
    for y in range(1, 10):
        if y == 1:
            ax1.axhline(y*10**x, xmin=0, xmax=1, linewidth=1, color='g')
        else:
            ax1.axhline(y*10**x, xmin=0, xmax=1, linewidth=0.5, color='g')

# ax1.set_xlabel('Frequency [Hz]')
# ax1.set_ylabel('Reactance [Ohm]')
ax1.set_ylim(2 * 10**imp_min_pow, 2 * 10**(imp_max_pow - 1))
ax1.set_xlim(10**freq_min_pow, 10**freq_max_pow)
ax1.tick_params(axis='x', pad=20)

# Plot the +10/10 (L) and -10/10 (C) lines
f = np.logspace(1, 9, int(1e3))
for x in range(-15, 1):
    for C in range(0, 10):
        X = 1 / (2 * np.pi * f * (C * 10 ** x))
        X[X <= 10**imp_min_pow] = 10**imp_min_pow
        X[X >= 10**imp_max_pow] = 10**imp_max_pow
        if C == 1:
            ax1.loglog(f, X, linewidth=1, color='b')
        else:
            ax1.loglog(f, X, linewidth=0.5, color='b')

for x in range(-12, 4):
    for L in range(0, 10):
        X = 2 * np.pi * f * (L * 10**x)
        X[X <= 10**imp_min_pow] = 10**imp_min_pow
        X[X >= 10**imp_max_pow] = 10**imp_max_pow
        if L == 1:
            ax1.loglog(f, X, linewidth=1, color='g')
        else:
            ax1.loglog(f, X, linewidth=0.5, color='g')

# Annotate Henrys and Farads
YH = np.array(['1pH', '10pH', '100pH', '1nH', '10nH', '100nH', '1$\mu$H',
               '10$\mu$H', '100$\mu$H', ''])
YF = np.array(['100nF', '10nF', '1nF', '100pF', '10pF', '1pF', '100fF',
               '10fF', '1fF', ''])
XH1 = np.array(['10$\mu$H', '1$\mu$H', '100nH', '10nH', '1nH', '100pH',
                '10pH', '1pH', '', ''])
XF1 = np.array(['', '1F', '100mF', '10mF', '1mF', '100$\mu$F', '10$\mu$F',
                '1$\mu$F', '', ''])
XH2 = np.array(['', '', '100H', '10H', '1H', '100mH', '10mH', '1mH', '', ''])
XF2 = np.array(['', '1nF', '100pF', '10pF', '1pF', '100fF', '10fF', '1fF',
                '', ''])

for x in range(imp_min_pow, imp_max_pow):
    ax1.text(1.1 * 10**freq_max_pow, 5.5 * 10**x, YH[x+3],
             fontsize=10,
             color='g',
             horizontalalignment='left')
    ax1.text(1.1 * 10**freq_max_pow, 1.4*10**x, YF[x+3],
             fontsize=10,
             color='b',
             horizontalalignment='left')

for x in range(freq_min_pow, freq_max_pow):
    ax1.text(3 * 10**x, 1.3 * 10**imp_min_pow, XH1[x-1],
             fontsize=10,
             color='g',
             horizontalalignment='center')
    ax1.text(0.8 * 10**x, 1.3 * 10**imp_min_pow, XF1[x-1],
             fontsize=10,
             color='b',
             horizontalalignment='center')

    ax1.text(3 * 10**x, 2.4 * 10**(imp_max_pow - 1), XH2[x-1],
             fontsize=10,
             color='g',
             horizontalalignment='center')
    ax1.text(0.8 * 10**x, 2.4 * 10**(imp_max_pow - 1), XF2[x-1],
             fontsize=10,
             color='b',
             horizontalalignment='center')

ax1.set_xticks([10**x for x in range(freq_min_pow, freq_max_pow+1)])
ax1.set_yticks([10**x for x in range(imp_min_pow+1, imp_max_pow)])
ax1.set_xticklabels(['10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz',
                    '10MHz', '100MHz', '1GHz'])
ax1.set_yticklabels(['10m$\Omega$', '100m$\Omega$', '1$\Omega$', '10$\Omega$',
                     '100$\Omega$', '1k$\Omega$', '10k$\Omega$',
                     '100k$\Omega$', '1M$\Omega$'])

# Adjust figure to A3 size paper
fig.tight_layout()
plt.subplots_adjust(left=0.05, right=0.96, top=0.97, bottom=0.06)
fig.set_size_inches((16.53, 11.69), forward=True)
fig.patch.set_facecolor('white')
plt.show()

# Print figure to pdf
pp = PdfPages('reactancechart.pdf')
pp.savefig(fig)
pp.close()
