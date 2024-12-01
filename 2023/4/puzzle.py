import sys, functools
import re
"""
"""
def score_card(line):
    w, h = line.split('|')
    winners = set([ int(n) for n in w.split(':')[1].split()
                    if n.isdigit()])
    have = set( [ int(n) for n in h.split()
                  if n.isdigit()])
    print(have&winners)
    # second puzzle:
    return len(have&winners)

def phase_one():
    if not (have & winners) :
        return 0
    else :
        return 2** (len(have&winners)-1)

def copycount(data):
    copies = [1] * len(data)
    for i in range(len(data)):
        score = score_card(data[i])
        for j in range(1,score+1):
            copies[i+j]+= copies[i]
    return sum(copies)
    
def main(args):
    data =  list(map(str.rstrip,open(args[0]).readlines()))
    #print(sum(map(score_card, data)))
    print(copycount(data))
    
if __name__ == '__main__':
    main(sys.argv[1:])
