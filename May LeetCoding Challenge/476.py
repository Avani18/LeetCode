# Number Complement
# https://leetcode.com/problems/number-complement/
# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

import math

def findComplement(num):
        number_of_bits = (int(math.floor(math.log(num) / math.log(2))) + 1)
        return ((1 << number_of_bits) - 1) ^ num
        
print(findComplement(5))
