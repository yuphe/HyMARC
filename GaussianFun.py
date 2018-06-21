"""
author : Yuping He
data : June 19, 2018
using Gaussian function to smooth the curve

Inputs:
fname: data file name
sigma: root mean square (width) for Gaussian distribution
xp : column number for data x
yp : column number for data y
"""

def Gaussian(data,sigma,xp,yp):
    import sys, math

    dx = data[1][xp] - data[0][xp]
    sgm = sigma * dx
    pref = 1.0 / (math.sqrt(2.0 * math.pi) * sgm)

    gdat = [[0.0, 0.0] for i in xrange(len(data))]

    for ix in range(len(data)):
        gdat[ix][0] = data[ix][xp]
        for jx in range(-len(data), len(data)):
            if ix + jx < 0 or ix + jx >= len(data):
                continue
            gdat[ix][1] += data[ix + jx][yp] * pref * math.exp(-(dx * jx) ** 2 / sgm ** 2 / 2) * dx

    return gdat