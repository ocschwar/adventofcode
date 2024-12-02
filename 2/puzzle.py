import sys
import argparse
import os
import copy

def main_1(args):
    L = open(args[1]).readlines()
    L = [list(map(int,l.split())) for l in L]
    A = sorted([l[0] for l in L])
    B = sorted([l[1] for l in L])
    ret = sum([abs(x-y) for (x,y) in zip(A,B)])
    print(ret)

def main_2(args):
    L = open(args[1]).readlines()
    L = [list(map(int,l.split())) for l in L]
    A = [l[0] for l in L]
    B = [l[1] for l in L]
    ret = 0
    for a in A:
        ret+= a* sum([ ( 1 if a==b else 0) for b in B])
    print(ret)
    
def deriv(report) :
    return [ x-y for (x,y) in zip(report[1:], report[:-1])]

def sign(n) :
    if n > 0 :
        return 1
    elif n == 0 :
        return 0
    else:
        return -1

def safe_report( report) :
    d = deriv(report)
    s = set(map(sign,d))
    m = max(map(abs,d))
    return ( 0 not in s and len(s) == 1 and m < 4)

def safe_levels(report):
    if safe_report(report):
        return True
    for i in range( len(report)):
        c = copy.copy(report)
        c.pop(i)
        if safe_report(c) :
            return True
    return False 
def main(args):
    L = open(args[1]).readlines()
    reports = [ list(map(int, line.split())) for line in L]
    s = list(map(safe_report,reports))
    print(s.count(True))
    s = list(map(safe_levels,reports))
    print(s.count(True))

if __name__ == "__main__":
    main(sys.argv)
