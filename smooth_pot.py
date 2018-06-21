import argparse
from GaussianFun import Gaussian

parser = argparse.ArgumentParser()
parser.add_argument("file",help="input potential file")
parser.add_argument("pair",nargs='+',help='a list of pair potentials')
parser.add_argument('-s', dest="sigma",type=float, help='a width for Gaussian smearing')
parser.add_argument('-x', dest="xp",type=int,help='column number for x')
parser.add_argument('-y', dest="yp",type=int,help='column number for y')

args = parser.parse_args()

fname = args.file
sigma = args.sigma
xp = args.xp
yp = args.yp

Npot = 0
data = []
nnn = 0
with open(fname,'r') as f1:
    for line in f1.readlines():
        nnn = nnn + 1
        if nnn == 4:
              Npot = int(line.split()[1])
        data.append(line.split())

print("Number of potential points:",Npot)

for i in range(len(data)):
    if len(data[i]) == 1:
        if data[i][0] == args.pair[0]:
            idx = i + 3
            fdx = idx + Npot
            temp = [map(float, l) for l in data[idx:fdx]]
            result = Gaussian(temp, sigma, xp, yp)


with open('smear.dat','w') as f2:
    for i in range(len(result)):
        print >>f2,'%.6f \t %.6f' % (result[i][0],result[i][1])
