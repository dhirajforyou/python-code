#!/usr/bin/env python

### Goal: Different implementations for Fibonacci number generation ###
### f(x) = f(x-1) + f(x-2)

import sys
import time
import math

# direct formula based implementation
def formula_based(num):
    golden_ratio = (1 + math.sqrt(5))/2
    val = (golden_ratio**num - (1 - golden_ratio)**num)/ math.sqrt(5)
    return int(round(val))

# single loop implementation
def single_loop(num):
    if num <= 0:
        return 0
    f0 = 0
    f1 = 1
    result = f0 + f1
    for i in range(1, num):
        result = f0 + f1
        f0 = f1
        f1 = result
    return result

# simple dynamic prog based implementation
def dynamic(num):
    result = [None] * (num+1)
    result[0] = 0
    result[1] = 1
    for i in range(2, num+1):
        result[i] = result[i-1] + result[i-2]
    return result[num]

# recursive implementation 
def rec_fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return rec_fibonacci(num-1) + rec_fibonacci(num -2)

# memoization is remembering the last computation, instead of recomputing
memoized = {}
def memoized_fibonacci(num):
    if num in memoized:
        return memoized[num]
    else:
        if num == 0:
            memoized[num] = 0
            return memoized[num]
        elif num == 1:
            memoized[num] = 1
            return memoized[num]
        else:
            val = memoized_fibonacci(num - 1) + memoized_fibonacci(num -2 )
            memoized[num] = val
            return memoized[num]


def main(args):
    i = input("Enter x for finding Fibonacci(x) \n")
    i = int(i)

    start = time.time()
    res = formula_based(i)
    time_taken = time.time() - start
    print res, "using formula, time taken", time_taken

    start = time.time()
    res = single_loop(i)
    time_taken = time.time() - start
    print res, "using raw, time taken", time_taken

    start = time.time()
    res = dynamic(i)
    time_taken = time.time() - start
    print res, "using dynamic, time taken", time_taken

    start = time.time()
    res = rec_fibonacci(i)
    time_taken = time.time() - start
    print res, "using rec fibonacci, time taken", time_taken

    start = time.time()
    res = memoized_fibonacci(i)
    time_taken = time.time() - start
    print res, "using memoized fibonacci, time taken", time_taken

if __name__=='__main__':
    main(sys.argv)

