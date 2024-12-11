import sys
import argparse
import os, re
import copy
import functools
import pprint

def blink(L):
    LC = copy.copy(L)
    ii = 0 
    for i,l in enumerate(L):
        if l == 0 :
            LC[i+ii] = 1
        else:
            s = str(l)
            if len(s)%2==0:
                a = s[:len(s)//2]
                b = s[len(s)//2:]
                print('SS',s,a,b)
                LC[i+ii] = int(a)
                LC.insert(i+ii+1, int(b))
                ii+=1
            else:
                LC[i+ii] =l* 2024
    return LC

def sub_blink(D):
    nd = {}
    for l,v in D.items():
        if not v:
            continue
        if l == 0 :
            nl = [1] 
        else:
            s = str(l)
            if len(s)%2==0:
                a = s[:len(s)//2]
                b = s[len(s)//2:]
                nl = [int(a),int(b)]
            else:
                nl =[l* 2024]
        for n in nl:
            nd[n] = nd.get(n,0) + v
    return nd 
        
    

def blink_2 (L):
    D = {}
    for l in L:
        D[l] =D.get(l,0) + 1
    return D

def main(args):
    LL = list(map(int,open(args[1]).readlines()[0].rstrip().split(' ')))
    #print(LL)
    #for i in range(int(args[2])):
    #    LL = blink(LL)
    #    print('LL',LL)    
    #    print('LL',len(LL))
    D = blink_2(LL)
    print(D, len(D))
    for i in range(int(args[2])):
        D = sub_blink(D)
        S = sum(D.values())
        print(i+1, D, S)
        
        
if __name__ == "__main__":
    main(sys.argv)
