# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
'''Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.'''

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s=[]
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.s:
            self.s.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.s:
            self.s.remove(val)
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r=random.randint(0,len(self.s)-1)
        return self.s[r]

