# Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
'''Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.'''


from collections import Counter

def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count.values():
            if i == 1:
                continue
            else:
                return list(count.keys())[list(count.values()).index(i)]
