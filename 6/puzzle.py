import sys
import math
import numpy
from functools import reduce
import re 
"""
ANother candidate for using Verus...
"""

def main_0(args):
    lines = open(args[0]).readlines()    
    ops = lines[-1]
    lines = lines[:-1]
    ops = ops.split()
    print(ops)
    lines = [list(map(int,line.split())) for line in lines]
    print(lines)
    s = 0 
    for i,op in enumerate(ops):
        nums = [lines[x][i] for x in range(len(lines))]
        if op == "+" :
            s += sum(nums)
        else:
            s += reduce(int.__mul__, nums)
    print(s)
    
def main(args):
    lines = open(args[0]).readlines()    
    ops = lines[-1]
    lines = lines[:-1]
    # alignment set by the opts character!
    ops_indices = list( re.finditer("[\*\+] +",ops))
    print(ops)
    print(ops_indices)
    cols = []
    for i,op in enumerate(ops_indices):
        col = [line[op.span()[0]:op.span()[1]] for line in lines]
        cols.append(col)
    print(cols)
    S = 0
    for i,op in enumerate(ops_indices):
        col = cols[i]
        l = op.span()[1]-op.span()[0]
        nums = []
        for c in range(l):
            s = ''.join([l[c] for l in col])
            if not s.isspace():
                nums.append(int(s.rstrip().lstrip()))
            #print('S',s)
        if ops[op.span()[0]] == "+" :
            X= sum(nums)
        else:
            X= reduce(int.__mul__, nums)
        S += X
        print(nums, i , X)
    print(S)
if __name__=="__main__":
    main(sys.argv[1:])
