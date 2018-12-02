#!/usr/bin/env python

### Goal is a task with timeline  ###

import sys
import io
import atexit

def read_data():
    # raw_input is normal way to take input
    # raw_input can take optional prompt argument
    # It strips the newline char from the string it returns
    nums = raw_input("How many numbers")
    array = [int(x) for x in raw_input("give me "+ str(nums) + "int numbers \n").split()]
    print array

def sys_stdin():
    # this is another way to read input data
    # similar to reading a file, where the file is stdin
    # input is not stripped
    n = sys.stdin.readline()
    print >> sys.stdout, "n is", n


buffer  = io.BytesIO()
#sys.stdout = buffer

def buffered_io():
    # this is booster for output
    # BytesIo allows to keep the data as bytes in an in-memory buffer as the variables
    n = int(raw_input("give me a number"))
    print >> buffer,  n

@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())


def main(args):
    #read_data()
    #sys_stdin()
    buffered_io()



if __name__=='__main__':
    main(sys.argv)

