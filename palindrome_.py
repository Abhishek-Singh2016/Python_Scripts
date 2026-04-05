#!/bin/python3

import math
import os
import random
import re
import sys

#- Step 1: Extract only letters → ['A','b','B','a'] 
#- Step 2: Convert to lowercase → ['a','b','b','a'] 
#- Step 3: Compare sequence forward and backward: 'abba' == 'abba' → true

#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Write your code here
    letters = []
    for _str in code:
        if (_str).isalpha():
            _str = _str.lower()
            letters.append(_str)
    #return letters == letters[::-1]
    print(letters)

    if letters == letters[::-1]:
        return True
    return False


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
