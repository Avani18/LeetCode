# Maximum Number of Balloons


from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if ('b' not in text) or ('a' not in text) or ("l" not in text) or ("o" not in text) or ("n" not in text):
            return 0
        count = Counter(text)
        minp = min(count['b'], count['a'], count['n'])
        while minp > 0:
            if count['l'] >= 2*minp and count['o'] >= 2*minp:
                return minp
            minp -= 1
        return 0
        
