# Backspace String Compare


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        str1 = ''
        str2 = ''
        
        for i in range(len(S)):
            if S[i] == '#':
                str1 = str1[:-1]
            else:
                str1 += S[i]
                
        for i in range(len(T)):
            if T[i] == '#':
                str2 = str2[:-1]
            else:
                str2 += T[i]
                
        if str1 == str2:
            return True
        return False
