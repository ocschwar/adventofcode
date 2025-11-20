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

RE = """Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)
"""
    
def main(args):
    LL = open(args[1]).read()
    L = re.findall(RE,LL)
    ret = 0 
    for r in L:
        l = tuple(map(int,r))
        print(l)
        #S = solve_det((l[0],l[1]),(l[2],l[3]),(l[4],l[5]))
        S = solve_det((l[0],l[1]),
                      (l[2],l[3]),
                      (10000000000000+l[4],10000000000000+l[5]))
        if check_det((l[0],l[1]),(l[2],l[3]),
                     (10000000000000+l[4],10000000000000+l[5]),S):
            ret += 3*S[0] +S[1]
    print(ret)
        
if __name__ == "__main__":
    main(sys.argv)
