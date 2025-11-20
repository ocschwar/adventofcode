import sys
import argparse
import os, re
import copy

def check_update(R, update) :
    print(R, update)
    check = [ update.index(r[0]) <=update.index(r[1]) for
              r in R]
    return all(check)
def add_updates(rules, update) :
    R = [ r for r in rules if r[0] in update and r[1] in update]    
    if check_update(R, update):
        return 0 #return update[len(update)//2]
    return fix_update(R,update)

def fix_update(R, u):
    print(u)
    order = {}    
    for m in u:
        order[m] = sum([ (
            1 if m == r[0] else -1 if m == r[0] else 0  
        )  for r in R])
    U = sorted(u, key = lambda x:-order[x])
    print(U)
    return U[len(U)//2]
    
def main(args):
    LL = open(args[1]).readlines()
    pipes = [l for l in LL if '|' in l]
    commas = [l for l in LL if ',' in l]
    rules = [ list(map(int,l.split('|'))) for l in pipes]
    updates = [ list(map(int, l.split(','))) for l in commas]
    
    ret = sum(map( lambda u: add_updates(rules, u), updates))
    print(ret)
if __name__ == "__main__":
    main(sys.argv)
