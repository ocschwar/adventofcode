import sys
import math

def invalid(s):
    l = len(s)
    if l%2 == 1 :
        return 0 
    Sa = s[:l//2]
    Sb = s[l//2:]
    if Sa == Sb:
        return int(s)
    else:
        return 0
    
def invalider(s, n):
    l = len(s)
    if l%n != 0 :
        return 0 
    Sa = s[:l//n]
    Sb = Sa * n 
    if s == Sb:
        return int(s)
    else:
        return 0

def invalidest(s):
    for i in range(2,len(s)+1):
        I = invalider(s,i)
        if I:
            return I
    return 0
    
def main(args):
    line = open(args[1]).read()
    ranges = [ r.split('-') for r in line.split(',')]
    S = 0 
    for R in ranges:
        r = range(int(R[0]), int(R[-1])+1)
        s = sum(map(lambda x: invalidest(str(x)), r))
        S+= s
    print(S)

if __name__=="__main__":
    main(sys.argv)
