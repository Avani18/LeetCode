# Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         for i in s:
#             if i in t:
#                 t = t.replace(i, '', 1)
#                 s = s.replace(i, '', 1)
                
#         if t.strip() == '' and s.strip() == '':
#             return True
        
#         return False

        return Counter(s) == Counter(t)
