# Check for Non-Identical String Rotation
# Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0.

# Example

# Input:

# s1 = abcde
# s2 = cdeab

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # Write your code here
    if s2 == s1:
        return False
    if len(s1) != len(s2):
        return False
    combined = s1 + s1
    if s2 in combined:
        return 1
    else:
        return 0

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))


