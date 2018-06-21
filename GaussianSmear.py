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
import sys, math
import argparse
parser = argparse.ArgumentParser(description="Gaussian smearing method")
parser.add_argument('fname',help="input file")
parser.add_argument('-s',dest="sigma",type=float,
                    default=2.0,help="width of Gaussian in the unit of dz")
parser.add_argument('-x',dest="xp",type=int,default=1,
                    help="position of x data (start from 1)")
parser.add_argument('-y',dest="yp", type=int,default=2,
                    help="position of y data (start from 1)")
args = parser.parse_args()

xp = args.xp-1
yp = args.yp-1
sigma = args.sigma
fname = args.fname

data = []
with open(fname,'r') as f1:
    for line in f1.readlines():
        data.append(map(float, line.split()[xp:yp+1]))

dx =  data[1][0]-data[0][0]
sgm = sigma*dx
pref = 1.0/(math.sqrt(2.0*math.pi)*sgm)

gdat = [[0.0,0.0] for i in xrange(len(data))]

for ix in range(len(data)):
    gdat[ix][0] = data[ix][0]
    for jx in range(-len(data),len(data)):
        if ix+jx < 0 or ix+jx >= len(data):
            continue
        gdat[ix][1] += data[ix+jx][1]*pref*math.exp(-(dx*jx)**2/sgm**2/2)*dx

with open(fname+".smeared",'w') as f2:
    for i in range(len(data)):
        print >>f2, '%.6f \t %.6f' % (gdat[i][0],gdat[i][1])

print('write'+fname+'smeared')
print('GAUSSIAN SMEAR DONE !')