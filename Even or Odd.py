# -*- coding: utf-8 -*-
"""
Created on Tue May 14 04:03:02 2019

@author: srsharma
"""

# wap given number is even or odd using bitwise operator
# Returns true if n
# is even, else odd
def isEven(n):
    # Return true if n/2 does not result in a float value.
    return (int(n / 2 ) * 2 == n)
    if(isEven(n) !=False):
        print("Even")
    else:
        print("odd")
        
        