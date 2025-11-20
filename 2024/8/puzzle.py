import sys
import argparse
import os, re
import copy
import functools
def list_nodes(ant):
    n = []
    for a in ant:
        for b in ant[1:]:
            if a == b:
                continue
            d = (a[0]-b[0], a[1]-b[1])
            N= [(a[0] + d[0], a[1]+d[1])]
            N += [(b[0] - d[0], b[1]-d[1])]
            print('A', a, b, N)
            n+= N
    return n
def in_bounds(a,I,J):
    return ( a[0] >= 0 and a[1]>= 0
             and a[0] < I and a[1] < J)
def list_nodes_2(ant, I, J):
    n = []
    for a in ant:
        for b in ant[1:]:
            n+= [a,b]
            if a == b:
                continue
            d = (a[0]-b[0], a[1]-b[1])                        
            N= (a[0] + d[0], a[1]+d[1])
            while in_bounds(N,I,J):
                n.append(N)
                N= (N[0] + d[0], N[1]+d[1])                
            N = (b[0] - d[0], b[1]-d[1])
            while in_bounds(N,I,J):
                n.append(N)
                N= (N[0] - d[0], N[1]-d[1])                
    return n 
def scan_ants(LL) :
    d = {}
    for i,l in enumerate(LL):
        for j,c in enumerate(l):
            if c != '.':
                d[c] = d.get(c,[]) + [(i,j)]
    return d 

def main(args):    
    LL = list(map( str.rstrip, open(args[1]).readlines()))
    I = len(LL)
    J = len(LL[0])
    d = scan_ants(LL)
    N = []
    for v in d.values():
        L = list_nodes(v)
        for n in L :
            if (n[0]>=0 and
                n[1]>=0 and 
                n[0]<I and
                n[1]<J):
                N.append(n)
    N = set(N)
    print(sorted(N))
    print(len(N))
    N = []
    for v in d.values():
        L = list_nodes_2(v,I,J)
        print(L)
        N += L
    N = set(N)
    print(len(N))
    #for k,v in d.items():
    #    print(k, v , list_nodes(v))
if __name__ == "__main__":
    main(sys.argv)
