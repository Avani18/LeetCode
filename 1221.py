# Split a String in Balanced Strings


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = lc = rc = 0
        for i in s:
            if i == 'L':
                lc += 1
            else:
                rc += 1
            if lc == rc:
                num += 1
                lc = rc = 0
                
        return num
