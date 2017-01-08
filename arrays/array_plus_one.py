#!/usr/bin/python
"""
a number is splitted as array(left most as most significant digit)
And Given that array, add 1 to the number.
ex. 1. [2,9,9] => [3,0,0]
ex. 2. [1,1,3] => [1,1,4]
"""

def plus_one(arr):
    """
    Add plus one to the array
    """
    if all(9 == num for num in arr):
        return [1]+ [0] * len(arr)
    for num in range(len(arr)-1,-1,-1):
        if arr[num] + 1 >9:
            arr[num] =0
        else:
            arr[num] +=1
            break
    return arr

print plus_one([2, 9, 9])
print plus_one([1, 2, 0, 6])
print plus_one([9, 9, 9])
