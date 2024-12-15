import sys
import argparse
import os, re
import copy
import functools
import pprint
import numpy
import math 

def solve_det( A, B , X):
    return (
        math.floor((X[0]*B[1]-X[1]*B[0])/(A[0]*B[1]-A[1]*B[0])), 
        math.floor((-X[0]*A[1]+X[1]*A[0])/(A[0]*B[1]-A[1]*B[0])), 
        )

def check_det(A,B,X,S):
    return ( S[0] * A[0] + S[1]*B[0] == X[0] and
             S[0] * A[1] + S[1]*B[1] == X[1])

def new_pos(P, V, n, I, J):
    NP = ( (P[0] + n * V[0])%I ,
           (P[1] + n * V[1] )%J)
    return NP
RE = "p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)"
QUADS = [ ((0,0), (49,51)) ,
          ((51,0), (100,51)) ,
          ((0,53), (49,102)) ,
          ((51,53), (100,102)) ]
def main(args):
    LL = open(args[1]).read()
    L = re.findall(RE,LL)
    R = [ tuple(map(int,l)) for l in L]
    p = [new_pos((r[0],r[1]),(r[2],r[3]),100,
                 int(args[2]),
                 int(args[3])) for r in R]
    print(p)
    Q = [0,0,0,0]
    x = int(args[2]) // 2 
    y = int(args[3]) // 2 
    for P in p:
        if P[0]< x :
            if P[1] < y:
                Q[0] += 1
            elif P[1] > y: 
                Q[1] += 1
        elif P[0]> x :
            if P[1] < y:
                Q[2] += 1
            elif P[1] > y: 
                Q[3] += 1

    print(functools.reduce(int.__mul__,Q))
if __name__ == "__main__":
    main(sys.argv)
