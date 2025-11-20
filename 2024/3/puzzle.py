import sys
import argparse
import os, re
import copy

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
    L = open(args[1]).read()
    muls = re.findall('mul\((\d+),(\d+)\)',L)
    print( sum( [int(a)*int(b) for (a,b) in muls]))
    filtered = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",L)
    do = 1
    ret = 0 
    for i in filtered:
        if i == 'do()':
            do = 1
        elif i == "don't()":
            do = 0
        else:
            m = re.match("mul\((\d+),(\d+)\)",i).groups()
            ret += do*int(m[0])*int(m[1])
    print(ret)
if __name__ == "__main__":
    main(sys.argv)
