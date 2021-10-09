# Valid Palindrome II
# 99.92% faster runtime

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        
        def check(s):
            if s == s[::-1]:
                return True
        
        left = 0
        right = len(s)-1
        
        while (left < right):
            if s[left] == s[right]:
                left += 1
                right -= 1
                
            elif check(s[:left]+s[left+1:]):
                return True
            
            elif check(s[:right]+s[right+1:]):
                return True
            
            else:
                return False
            
        return False
