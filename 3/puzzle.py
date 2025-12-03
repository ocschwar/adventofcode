import sys
import math

def max_jolt(bank):
    M = max(enumerate(bank[:-1]),
            key = lambda x: x[1])
    m = max(bank[M[0]+1:])
    print(M,m)
    return 10*M[1]+m 

def rec_jolt(bank,I):
    ret = []
    s = -1
    #print(bank, len(bank))
    while len(ret) < I :
        # options:
        # s+1 : options: len(bank) - s
        # first case: 14 left, for 11
        e =  -I+len(ret)+1
        end = ( e if e<0 else None)
        #print(s,e,list(enumerate(bank))[s+1:end ])
        M = max(list(enumerate(bank))[s+1:end ],
                key = lambda x: x[1])
        ret.append(M[1])
        s = M[0]
        # 
        #print(ret,s, bank[s:],end )
    #print(ret)    
    return int(''.join(map(str,ret)))
def main(args):
    lines = open(args[1]).readlines()
    banks = list(map(lambda line: list(map(int, line[:-1])), lines))
    #print(banks)
    print(sum(map(lambda x: rec_jolt(x, 12), banks)))
    
    
    
def main_0(args):
    lines = open(args[1]).readlines()
    banks = list(map(lambda line: list(map(int, line[:-1])), lines))
    print(banks)
    print(sum(map(max_jolt, banks)))

if __name__=="__main__":
    main(sys.argv)
