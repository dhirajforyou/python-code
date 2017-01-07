#!/usr/bin/python
"""
https://leetcode.com/problems/rotate-array/
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

def do_reverse(start, end, arr):
    """
    Given start and end, reverses the elements
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def main():
    """
    Main Function
    """
    print "Enter numbers delimited by space"
    arr = [int(x) for x in raw_input().split(' ')]
    k = int(raw_input("Rotate by:"))
    n = len(arr)
    k = k % n 
    do_reverse(0, n-k-1, arr)
    do_reverse(n-k, n-1, arr)
    do_reverse(0, n-1, arr)
    print ' '.join([str(x) for x in arr])

if __name__ == '__main__':
    main()
