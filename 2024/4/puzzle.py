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

def find_cadence(LL, i, j, c, phrase) :
    #print(len(LL), len(LL[i]), i,j,c,phrase)
    if (c[0] != 0 and ( i+c[0]*len(phrase) > len(LL) or
         i + c[0]*len(phrase) < -1 )):
        return 0
    if (j+c[1]*len(phrase) > len(LL[i]) or
        j+c[1]*len(phrase) <-1) and c[1] != 0 :
        return 0
    test = ''.join([ LL[i+x*c[0]][j+x*c[1]] for x in range(len(phrase))])
    ret = (1 if test == phrase else 0 )
    #print(len(LL), len(LL[i]), i,j,c,phrase, test, ret)
    return ret
    

def find_xmas( LL, i, j, phrase='XMAS') :
    cadences = [ [1,0], [-1,0], [0,1] , [0,-1],
                 [1,1], [1,-1], [-1,1], [-1,-1]]
    return sum([ find_cadence(LL, i, j, c, phrase) for c in cadences])

def find_x_mas(LL, i, j, phrase='MAS') :
    if LL[i][j] != 'A':
        return 0
    s = ''.join([ LL[i-1][j-1], LL[i-1][j+1],
                  LL[i+1][j-1], LL[i+1][j+1]])
    print (i,j,s, LL[i][j])
    if s in ('MSMS', 'SMSM', 'SSMM', 'MMSS'):
        return 1
    return 0 
def main(args):
    LL = open(args[1]).readlines()
    s = 0 
    for i in range(len(LL)):
        for j in range(len(LL[i])):
            s += find_xmas(LL,i,j,'XMAS')
    
    print(s)
    s = 0 
    for i in range(1, len(LL)-1):
        for j in range(1,len(LL[i])-1):
            s += find_x_mas(LL,i,j,'MAS')
        #break
    print(s)
    
if __name__ == "__main__":
    main(sys.argv)
