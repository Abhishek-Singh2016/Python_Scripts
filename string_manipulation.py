s = "Gemini"
# Using Slicing
reversed_s = s[::-1]

print(f"Original: {s} | Reversed: {reversed_s}")

def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
    

print(are_anagrams("Listen", "Silent")) # True



def first_unique(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        print(counts)
    
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_unique("iiiiiwpst")) # 'w'


# compress string "aaabbcaaa" → "a3b2c1a3"
def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    # Append the last character and its count
    compressed.append(s[-1] + str(count))
    
    return ''.join(compressed)


print(compress_string("aaabbcaaa")) # "a3b2c1a3"




# Iterative (Efficient)
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Recursive (Elegant but slow for large n)
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

fib_iterative(10)

import math

n = 5
# Method 1: Built-in
print(math.factorial(n)) 

# Method 2: Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(n))