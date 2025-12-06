import sys
import math
import numpy 
"""
ANother candidate for using Verus...
"""
def inrange(ranges, elt):
    return(any([ elt in r for r in ranges]))

def runion(a,b):
    return range(a.start, max(a.stop,b.stop))
def main_0(args):
    lines = list(map(str.rstrip, open(args[1]).readlines()))
    ranges = [ l.split('-') for l in lines if '-' in l]
    ranges = [ range(int(s[0]),int(s[-1])+1) for s in ranges]
    checklist = [int(l) for l in lines if l and '-' not in l]
    ret = 'XXX'
    checklist = filter(lambda x: inrange(ranges,x),
                       checklist)
    print(len(list(checklist)))

def merge_ranges(ranges):
    mranges = []
    ret = False
    for r in zip(ranges[::2],ranges[1::2] ):
        print(r)
        if r[0].stop >= r[1].start:
            ret = True
            mranges.append( runion(r[0],r[1]))
        else:
            mranges.append(r[0])
            mranges.append(r[1])
    if len(ranges) % 2 == 1 :
        mranges.append(ranges[-1])
    return mranges,ret
def merge_ranges(ranges):
    mranges = []
    ret = False
    i = 1 
    while i < len(ranges):
        a = ranges[i-1]
        b = ranges[i]
        if a.stop >= b.start:
            ret = True
            print("X",a,b)
            mranges.append(runion(a,b))            
            i+=1
        else:
            mranges.append(a)
        i+= 1
    a = mranges[-1]
    b = ranges[-1]
    if b.stop > a.stop:
        mranges.append(b)
    print(mranges)
    return mranges,ret

def main(args):
    lines = list(map(str.rstrip, open(args[1]).readlines()))
    ranges = [ l.split('-') for l in lines if '-' in l]
    ranges = [ range(int(s[0]),int(s[-1])+1) for s in ranges]
    checklist = [int(l) for l in lines if l and '-' not in l]
    ret = 'XXX'
    checklist = filter(lambda x: inrange(ranges,x),
                       checklist)
    print(len(list(checklist)))
    ranges.sort(key=lambda x:x.start)
    print(ranges)
    mranges = merge_ranges(ranges)
    while mranges[1] :
        mranges = merge_ranges(mranges[0])        
    print(mranges)
    print(sum(map(len,mranges[0])))
    return
    S = set()
    for r in ranges:
        S = S.union(set(r))
    print(len(S))
if __name__=="__main__":
    main(sys.argv)
