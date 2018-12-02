#!/usr/bin/env python

# faster computations are not always better, as you make cpu to word hard
# bits and bytes are some hidden shortcuts to take out that hardness



# 1 << n, this is bitwise left shift by n bits
# so 1 << 2 is 100 which is 4
# also after left shift, every bit is shifted to left and blank position is replaced by 0, Since every bit is power of 2, with each shift every bit, number is getting dubbled or its getting multiplied by 2 :)
# 1 >> n, this is bitwise right shift by n bits
# so 16 >> 2 is 00100 which is 4
# also after right shift, every bit is shifted right and sign bit is placed at empty position. so sign bit 0 in case of positive and signbit 1 in case of negative sign. with every right shift, every bit value is reduced by factor oof 2, which is equivalent to dividing. and ultimately the whole number is getting divided by 2 with each shift
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

