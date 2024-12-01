import sys, functools
import re
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def is_part_no( row, start, end, data):
    """
    """
    top_left = [ max(row-1, 0 ), max(start-1,0)]
    bottom_right = [ min(row+2,len(data)), end+1]
    check= ''
    for row in range(top_left[0],bottom_right[0]):
        check +=data[row][top_left[1]: bottom_right[1]]
    return not bool(re.search("^[\d\.]+$",check))

def find_nums(rownum,data):
    ret = []
    line = data[rownum]
    M = re.finditer('\d+', line)
    for m in M:
        if is_part_no(rownum, m.start(), m.end(), data):
            print (int(m.string[m.start():m.end()]))
            ret.append(int(m.string[m.start():m.end()]))
    print(ret)
    return ret
def find_str_nums(rownum,data):
    ret = []
    line = data[rownum]
    M = re.finditer('\d+', line)
    for m in M:
        if is_part_no(rownum, m.start(), m.end(), data):
            #print (int(m.string[m.start():m.end()]))
            ret.append(m)
    return ret

def find_gears(rownum, data):
    ret=0
    str_nums=[]
    all_str_nums=[]
    line = data[rownum]
    stars = re.finditer('\*', line)
    if stars: 
        for row in range( max(rownum -1,0), min(rownum+2, len(data))):
            all_str_nums += find_str_nums(row,data)
    print(rownum)
    for star in stars:
        str_nums = [ m for m in all_str_nums if
                     (star.start() >= m.start() -1 ) and
                     (star.start() <= m.end() )]
        print(str_nums)
        if len(str_nums) == 2:            
            a = str_nums[0]
            b = str_nums[1]
            print(a,b)
            ret += (int(a.string[a.start():a.end()])*
                    int(b.string[b.start():b.end()]))
    return ret
                              

def foo():
    M = re.finditer('\d+', line)
    return sun(functools.reduce, set.__add__, 
        [ int(m.string[m.start():m.end()])
          for m in M if
          is_part_no(rownum, m.start(), m.end(), data)])

        
def main(args):
    #print(sum(map(check_ids, open(args[0]).readlines())))
    data =  list(map(str.rstrip,open(args[0]).readlines()))
    #print(sum(functools.reduce(list.__add__,
    #                           [ find_nums(i,data) for i in range(len(data))])))
    print(sum(
        [ find_gears(i,data) for i in range(len(data))]))
    
if __name__ == '__main__':
    main(sys.argv[1:])
