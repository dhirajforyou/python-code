#!/usr/bin/env python

# faster computations are not always better, as you make cpu to word hard
# bits and bytes are some hidden shortcuts to take out that hardness



# 1 << n, this is bitwise left shift by n bits
# so 1 << 2 is 100 which is 4
# 1 >> n, this is bitwise right shift by n bits
# so 16 >> 2 is 00100 which is 4
# 1 is 0000 0001, so ~1 is 1111 1110

import sys

def bin8(num):
    bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
    return bin8(num)

def mask_from_lsb(pos):
    mask = ~(( 1 << pos+1 ) -1)
    return mask

def clear_bits_from_lsb(num, pos):
    return num & mask_from_lsb(pos)

def mask_from_msb(pos):
    mask = (1 << pos) -1
    return mask

def clear_bits_from_msb(num, pos):
    return num & mask_from_msb(pos)
    
def main(args):
    num = input("Enter number\n")
    num = int(num)
    print "num is ", num, " in binary ", bin8(num)
    cleared_lsb  = clear_bits_from_lsb(num, 4)
    print "after clearing 4 pos from lsb ", cleared_lsb, " which is in bin", bin8(cleared_lsb)
    cleared_msb  = clear_bits_from_msb(num, 4)
    print "after clearing 4 pos from msb ", cleared_msb, " which is in bin", bin8(cleared_msb)
    print "start coding..."


if __name__=='__main__':
    main(sys.argv)

