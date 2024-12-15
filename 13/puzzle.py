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
        math.floor(X[0]*B[1]-X[1]*B[0])/(A[0]*B[1]-A[1]*B[0]), 
        math.floor(-X[0]*A[1]+X[1]*A[0])/(A[0]*B[1]-A[1]*B[0]), 
        )

def check_det(A,B,X,S):
    return ( S[0] * A[0] + S[1]*B[0] == X[0] and
             S[0] * A[1] + S[1]*B[1] == X[1])


def solve( A, B, X) :
    # ratio is 3...
    # so start with B... 
    top_b = min ([ X[0]//B[0] , X[1]//B[1] ])
    a = 0
    solved = False
    while not solved: 
        while ( X[0] > a*A[0] + top_b*B[0] and
                X[1] > a*A[1] + top_b*B[1]):
            a+=1
        if  ( X[0] == a*A[0] + top_b*B[0] and
              X[1] == a*A[1] + top_b*B[1]):
            solved = True
        else:
            while not ( X[0] > a*A[0] + top_b*B[0] and
                        X[1] > a*A[1] + top_b*B[1]):
                top_b -= 1
        if top_b < 0 or 100 < a+top_b:
            return None
    return (a,top_b)
    
def main(args):
    LL = list(map(str.rstrip,open(args[1]).readlines()))
    I = len(LL)
    J = len(LL[0])
    # region size for each plot
    RR = numpy.ones([I,J],dtype=int) * -1 
    # fencing price for each plot. 
    plants = set(list(functools.reduce(str.__add__,LL)))
    print(plants, RR)
    D = {}
    nregions = 0 
    for i in range(I):
        for j in range(J):
            ret =find_region(LL,(i,j),I,J,RR, nregions)
            if ret:
                pprint.pprint(("FF",RR,LL,ret))
                nregions = ret[0]+1 
                D[ret[0]] = {
                    'size':ret[1],'pts':ret[2]}
    for k,v in D.items():
        sides = count_sides(LL, v['pts'], I, J,RR)
        v['sides']=sides
    pprint.pprint(D)
    price = sum([v['size']*v['sides'] for v in D.values()])
    print('price',price)
        
if __name__ == "__main__":
    main(sys.argv)
