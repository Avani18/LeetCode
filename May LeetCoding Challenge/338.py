# Counting Bits
# https://leetcode.com/problems/counting-bits/
'''Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.'''


def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans = [0, 1]
        bits = 2
        while 2 ** bits <= num:
            ans += [j+1 for j in ans]
            bits += 1
        remains = num - 2 ** (bits-1) + 1
        ans += [ans[i] + 1 for i in range(remains)]
        return ans
