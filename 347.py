# Top K Frequent Elements
# 99.21% runtime

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [i[0] for i in counter.most_common(k)]
