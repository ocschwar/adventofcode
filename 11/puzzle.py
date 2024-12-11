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

def main(args):
    LL = list(map(int,open(args[1]).readlines()[0].rstrip().split(' ')))
    print(LL)
    for i in range(int(args[2])):
        LL = blink(LL)
        print('LL',LL)
        print(len(LL))
        
if __name__ == "__main__":
    main(sys.argv)
