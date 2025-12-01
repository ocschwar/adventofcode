import sys
import math


def main_1(args):
    lines = open(args[1]).readlines()
    start = 50
    hits = 0 
    dirs = {"R":1, "L":-1}
    for l in lines:
        start += dirs[l[0]] * int(l[1:])
        start %= 100
        if start == 0 :
            hits +=1 
    print(start, hits)
def main(args):
    lines = open(args[1]).readlines()
    start = 50
    hits = 0
    twits = [0,0,0]
    dirs = {"R":1, "L":-1}
    for l in lines:
        move = int(l[1:])
        sign = dirs[l[0]]
        hits += move//100
        twits[2] += move//100
        mod = move % 100
        if start > 0 : 
            if sign == 1 and start + mod >= 100 :
                twits[0] += 1 
                hits+=1
            elif sign == -1 and start - mod <= 0 :
                twits[1] += 1 
                hits += 1
        start += sign*move
        start %= 100 
    print(start, hits, twits)
        


if __name__=="__main__":
    main(sys.argv)
