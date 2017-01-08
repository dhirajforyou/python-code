#!/usr/bin/python
"""
Given array of numbers, shift(bubble down) zeros to end.

1. Do inplace
2. minimize operation required.
"""

def bubble_down(arr):
    back_index = 0
    front_index = 1
    n = len(arr)
    while front_index < n:
        if arr[back_index] == 0:
            if arr[front_index] != 0:
                arr[front_index], arr[back_index] = arr[back_index], arr[front_index]
                front_index += 1
                back_index += 1
            else:
                front_index += 1
        else:
            back_index += 1
            front_index += 1
    return arr

print bubble_down([0, 1, 0, 2, 3])
