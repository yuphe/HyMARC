import argparse
from GaussianFun import Gaussian

parser = argparse.ArgumentParser()
parser.add_argument("file",help="input potential file")
parser.add_argument("pair",nargs='+',help='a list of pair potentials')
parser.add_argument('-s', dest="sigma",type=float, help='a width for Gaussian smearing')
parser.add_argument('-r', dest="rp",type=int,help='column number for distance')
parser.add_argument('-p', dest="pp",type=int,help='column number for potential')
parser.add_argument('-f', dest="fp",type=int,help='column number for force')

args = parser.parse_args()

fname = args.file
sigma = args.sigma
pair = args.pair
rp = args.rp-1
pp = args.pp-1
fp = args.fp-1

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

for p in range(len(pair)):
    for i in range(len(data)):
        if len(data[i]) == 1:
            if data[i][0] == args.pair[p]:
                idx = i + 3
                fdx = idx + Npot
                temp = [map(float, l) for l in data[idx:fdx]]
                pot  = Gaussian(temp, sigma, rp, pp)
                force = Gaussian(temp, sigma, rp, fp)
                for k in range(Npot):
                    data[idx + k][1] = pot[k][0]
                    data[idx + k][2] = pot[k][1]
                    data[idx + k][3] = force[k][1]


with open('smear_table','w') as f2:
    for i in range(len(data)):
        print >>f2, "  ".join(map(str, data[i]))
