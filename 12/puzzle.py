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
    start = s = sorted(S)[0]
    c =LL[s[0]][s[1]]
    sides = 1
    d = (-1,0)
    nbrs = set()
    while True: 
        r = rots[d]
        N = (s[0]+d[0], s[1]+d[1])
        if ( N[0] >= 0 and N[1] >= 0 and
             N[0] <J and N[1] <J):
            nbrs.add(RR[N[0]][N[1]])
        else:
            nbrs.add(-1)
        P = (s[0]+r[0], s[1]+r[1])
        print(c, s, 'd', d, 'r', r,'P', P, P in S, sides)
        if P in S:
            P_ = (P[0]+d[0], P[1]+d[1])
            print(c,'2',s, d, r,P, P_, P_ in S)
            if P_ in S:
                # left turn!
                sides += 1
                s = P_
                d = rots[rots[r]]#(-d[0],-d[1])
                print("LEFT", P_, d )
                if s == start:
                    sides+=1
            else:
                s = P
        else:
            print("RT")
            # right turn.
            sides += 1
            d = r
        if sides>3 and s == start:
            break
    return (sides-sides%2,nbrs)
            
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
        sides,nbrs = count_sides(LL, v['pts'], I, J,RR)
        v['sides']=sides
        v['nbrs'] = nbrs
    price = sum([v['size']*v['sides'] for v in D.values()])
    print('price',price)
    pprint.pprint(("D",D))
    for k,v in D.items():
        if len(v['nbrs'])==1 :
            N = list(v['nbrs'])[0]
            if N == -1 :
                continue
            if k in D[N]['nbrs']:
                print('SKIP',k, v,D[N]['size'])
                continue
            price+= v['sides'] * D[N]['size']
    print('price',price)
    return

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
