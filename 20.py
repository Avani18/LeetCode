# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s) % 2 != 0):
            return False
        
        stack = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if stack:
                    if opening.index(stack[-1]) == closing.index(c):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False
