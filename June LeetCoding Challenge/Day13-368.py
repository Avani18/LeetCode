# Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/discuss/685816/python-trie-180-ms
'''Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.'''

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        trie = {}
        
        for n in nums:
            stack = [trie]
            
            while stack:
                node = stack.pop()
                found = False
                for key in node:
                    if n%key == 0:
                        found = True
                        stack.append(node[key])
                if not found:
                    node[n] = {}
                    
        self.res = []
        self.travel(trie, [])

            
        return self.res
    
def travel(self, node, curr):
        
        if len(self.res)< len(curr):
            self.res = list(curr)
        
        for key in node:
            curr.append(key)
            self.travel(node[key], curr)
            curr.pop()
