# Unique Number of Occurrences


from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        print (list(count.values()))
        print (list(set(count.values())))
        if len(set(count.values())) == len(count.values()):
            return True 
        else:
            return False
