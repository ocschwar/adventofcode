import sys
import argparse
import os, re
import copy
import functools
import pprint
import numpy

dirs = [ (1,0), (0,1),(-1,0), (0,-1)]
rots = { (1,0):(0,-1),
         (0,1):(1,0),
         (-1,0):(0,1),
         (0,-1):(-1,0)}
ddirs = dirs + [ (1,1),(-1,1), (1,-1), (-1,-1)]
def count_fences(LL, P, I, J, FF):
    c = LL[ P[0]][P[1]]
    ret = 0 
    for d in dirs:
        pp = (P[0]+d[0],P[1]+d[1])
        if (pp[0] < 0 or
            pp[1] < 0 or
            pp[0] >= I or 
            pp[1] >= J or
            LL[ pp[0]][pp[1]] != c
            ):
            ret+=1
    FF[P[0]][P[1]] = ret
    return ret
def count_sides(LL, S,I,J, RR):    
    corners = 0
    for s in S:
        up = (s[0] -1 ,s[1]) 
        lt = (s[0] ,s[1]-1 )
        dn = (s[0] +1 ,s[1]) 
        rt = (s[0] ,s[1]+1 )
        if (up not in S and lt not in S):# and (s[0]-1,s[1]-1) not in S):
            corners += 1
        if (dn not in S and rt not in S):# and (s[0]-1,s[1]-1) not in S):
            corners += 1
        if (up not in S and rt not in S):# and (s[0]-1,s[1]-1) not in S):
            corners += 1
        if (dn not in S and lt not in S):# and (s[0]-1,s[1]-1) not in S):
            corners += 1
        #if (dn not in S and rt not in S):            
        #    corners += 2
        #else:
        if (up in S and lt in S and (s[0]-1,s[1]-1) not in S):
            corners += 1
        if (dn in S and rt in S and (s[0]+1,s[1]+1) not in S):
            corners += 1
        if (up in S and rt in S and (s[0]-1,s[1]+1) not in S):
            corners += 1
        if (dn in S and lt in S and (s[0]+1,s[1]-1) not in S):
            corners += 1
    return corners
    # top left square, so it's facing "north".
    # and the side runs east...
    
def find_region(LL, P, I, J, RR, nregions ):
    if RR[ P[0]][P[1]] !=-1:#is not None:
        return None
    c = LL[ P[0]][P[1]]
    S = set()
    S.add(P)
    while True:
        ns = set()
        for p in S:
            for d in dirs:
                pp = (p[0]+d[0],p[1]+d[1])
                if pp in S:
                    continue
                if (pp[0] < 0 or
                    pp[1] < 0 or
                    pp[0] >= I or 
                    pp[1] >= J):
                    continue
                print(pp, I, J, c  )
                if LL[ pp[0]][pp[1]] == c:
                    ns.add(pp)
        if not ns:
            break
        S = S|ns
    size = len(S)
    pprint.pprint((RR,size))
    for P in sorted(S):
        print('pp',P, size)
        RR[ P[0]][P[1]] = nregions 
    pprint.pprint(RR)
    return nregions, size, S  
        

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

def foo():
    D = {}
    for i in range(I):
        for j in range(J):
            #ret += RR[i][j]* count_fences(LL, (i,j),I,J,FF)
            ret = count_sides(LL, (i,j),I,J,FF)            
    print(FF * (RR==12))
    print(ret)
    
        
if __name__ == "__main__":
    main(sys.argv)
