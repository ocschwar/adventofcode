import sys
import re 
def elevator( s) :
    return s.count('(') - s.count(')')

def position(s) :
    for i in range(0, len(s)):
        if elevator(s[:i]) < 0 :
            break
    return i

NUMBERS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
re_number = '(?=('+'|'.join(NUMBERS) + '|\d))'
numd = dict([ (v,k+1) for (k,v) in enumerate(NUMBERS)])
print(numd)

def digits_one(s):
    #M = list(map(int, filter(bool, re.split("\D+", s))))
    M = list(map(int, filter(str.isdigit, list(s))))
    print(s, M)
    return( 10*M[0] + M[-1])

def digits_two(s):
    print(s, re_number)
    M = re.findall(re_number,s)
    print(M)
    #M = list(map(int, filter(bool, re.split("\D+", s))))
    #M = list(map(int, filter(str.isdigit, list(s))))
    M = list(map(lambda x: int(x) if x.isdigit() else numd.get(x),
                 M))
    ret =( 10*M[0] + M[-1])
    print(s.rstrip(), M, ret)
    return ret
    
def main(args):
    #print( [elevator(open(a).read() ) for a in args])
    print(sum( [ digits_two(l) for l in (open(args[0]).readlines() )]))
if __name__ == '__main__' :
    main(sys.argv[1:])
