import sys
import re
import argparse

def puzz_to_ints(path):
    L = open(path).readlines()
    L = [list(map(int,l.split())) for l in L]
    return L

def sign(n) :
    if n > 0 :
        return 1
    elif n == 0 :
        return 0
    else:
        return -1

if __name__ == "__main__":
    print("welcome to aoc")
