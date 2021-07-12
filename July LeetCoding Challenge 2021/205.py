# Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        seen = dict()
        for i in range(len(s)):
            if s[i] in seen.keys():
                if t[i] == seen[s[i]]:
                    continue
                else:
                    return False
            elif t[i] in seen.values():
                return False
            else:
                seen[s[i]] = t[i]
        return True
