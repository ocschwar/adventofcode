import sys, functools

"""
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
Game 1: 13 green, 3 red; 4 red, 9 green, 4 blue; 9 green, 10 red, 2 blue

"""
limits = { 'red':12, 'green':13,'blue':14 }

def check_ids(s):
    gid = int(s.split(':')[0].split()[-1])
    rounds = s.split(':')[-1].split(';')
    for r in rounds:
        for d in r.split(','):
            n,c = d.split()
            if int(n) > limits[c]:
                return 0
    return gid

def poset(s):
    gid = int(s.split(':')[0].split()[-1])
    rounds = s.split(':')[-1].split(';')
    pos =  { 'red':1, 'green':1,'blue':1 }
    for r in rounds:
        for d in r.split(','):
            n,c = d.split()
            pos[c] = max([int(n), pos[c]])
    return functools.reduce(int.__mul__, pos.values())

def main(args):
    #print(sum(map(check_ids, open(args[0]).readlines())))
    print(sum(map(poset, open(args[0]).readlines())))
    
if __name__ == '__main__':
    main(sys.argv[1:])
