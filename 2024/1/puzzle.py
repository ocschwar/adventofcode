import sys
import argparse
import os

def main_1(args):
    L = open(args[1]).readlines()
    L = [list(map(int,l.split())) for l in L]
    A = sorted([l[0] for l in L])
    B = sorted([l[1] for l in L])
    ret = sum([abs(x-y) for (x,y) in zip(A,B)])
    print(ret)

def main_2(args):
    L = open(args[1]).readlines()
    L = [list(map(int,l.split())) for l in L]
    A = [l[0] for l in L]
    B = [l[1] for l in L]
    ret = 0
    for a in A:
        ret+= a* sum([ ( 1 if a==b else 0) for b in B])
    print(ret)

if __name__ == "__main__":
    main_2(sys.argv)
