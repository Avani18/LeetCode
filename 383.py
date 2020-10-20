# Ransom Note


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        
        for ele, c in rc.items():
            if c <= mc[ele]:
                continue
            else:
                return False
        return True
