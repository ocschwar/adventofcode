import sys
import argparse
import os, re
import copy
import functools
import pprint
def starts(LL):    
    S = []
    for i,L in enumerate(LL):
        for j,s in enumerate(L):
            if s == 0:
                S.append((i,j))
    return S

dirs = [ (-1,0),(0,-1), (0,1), (1,0)]
def search(LL,i,j,I,J):
    if LL[i][j] == 9 :
        return  LL[i][j]
    nxt = [ (i+d[0],j+d[1]) for d in dirs if
            i+d[0]>=0 and i+d[0] < I and
            j+d[1]>=0 and j+d[1] < J and            
            LL[i+d[0]][j+d[1]] - LL[i][j] == 1 ]
    return dict( [(d,search(LL, d[0], d[1], I,J))
                          for d in nxt])

def count_1(k, v, s):
    #print('s',k,v)
    if v == 9:
        return 1 #s.add(k)
    elif v == {}:
        return 0 # None
    else:
        #ret =  ([count(K,V,s) for K,V in v.items()])
        return sum([count_1(K,V,s) for K,V in v.items()])
    #return s
def count_2(k, v, s):
    #print('s',k,v)
    if v == 9:
        s.add(k)
    elif v == {}:
        return None
    else:
        ret = ([count_2(K,V,s) for K,V in v.items()])
        #return sum([count_2(K,V,s) for K,V in v.items()])
    return s
def main(args):    
    LL = list(
        map(str.rstrip,open(args[1]).readlines())) # [0].rstrip()
    LL = [ list(map(int, l)) for l in LL]
    print(LL)
    I = len(LL)
    J = len(LL[0])
    S = starts(LL)
    print (S)
    s_1 = 0
    s_2 = 0 
    for P in S:
        SR = {P:search(LL, P[0],P[1], I,J)}
        pprint.pprint (SR)
        d = count_1(P, SR, set([]))
        print('d',d)
        s_1+= d
        d = count_2(P, SR, set([]))
        print('d1',d)
        s_2+= len(set(d))
    print('s',s_1,s_2)
        
if __name__ == "__main__":
    main(sys.argv)
