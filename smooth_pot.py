import argparse
from GaussianFun import Gaussian

parser = argparse.ArgumentParser()
parser.add_argument("file",help="input potential file")
parser.add_argument("pair",nargs='+',help='a list of pair potentials')
parser.add_argument('-s', dest="sigma",help='a width for Gaussian smearing')
parser.add_argument('-x', dest="xp",help='column number for x')
parser.add_argument('-y', dest="yp",help='column number for y')

args = parser.parse_args()

Npot = 0
data = []
nnn = 0
with open(args.file,'r') as f1:
    for line in f1.readlines():
        nnn = nnn + 1
        if nnn == 4:
              Npot = int(line.split()[1])
        data.append(line.split())

print("Number of potential points:",Npot)

for i in range(len(data)):
    if len(data[i]) == 1:
        if data[i][0] == args.pair[0]:
            idx = i+3
            fdx = idx+Npot
            temp = Gaussian(data[idx:fdx],args.sigma,args.xp,args.yp)

print(temp)