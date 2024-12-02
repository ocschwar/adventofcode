import sys
import argparse
import os

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
    d = deriv(report)
    s = list(map(sign,d))
    m = list(map(abs,d))
    if len(set(s)) == 1 and max(m) < 4 and 0 not in s:
        return True
    else:        
        good_dir = (1 if s.count(1) > s.count(-1) else -1)
        s = [ i == good_dir for i in s]
        over = [ False if i>3 else True for i in m]
        anded = [ x and y for (x,y) in zip(s,over)]        
        print( """r{}
        {}
        {}
        {}
        {}""".format(report,d,s,over, anded))
        if anded.count(False) == 1:
            report.pop(anded.index(False))
            print(report)
            ret =  safe_report(report)
        else:
            ret = anded.count(False) == 0
        print(ret)
def main(args):
    L = open(args[1]).readlines()
    reports = [ list(map(int, line.split())) for line in L]
    s = list(map(safe_report,reports))
    print(s.count(True))
    s = list(map(safe_levels,reports))
    print(s.count(True))

if __name__ == "__main__":
    main(sys.argv)
