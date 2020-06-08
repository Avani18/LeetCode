# Power of Two
# https://leetcode.com/problems/power-of-two/
'''Given an integer, write a function to determine if it is a power of two.'''

def isPowerOfTwo(self, n: int) -> bool:
        return bin(n).count('1') == 1 and n > 0
