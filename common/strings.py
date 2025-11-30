import sys
import re
import argparse

def puzz_to_ints(path):
    L = open(path).readlines()
    L = [list(map(int,l.split())) for l in L]
    return L 
