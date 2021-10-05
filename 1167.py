# Minimum Cost to Connect Sticks

import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
#         ans = 0
        
#         while (len(sticks) != 1):
#             sticks.sort()
#             ans += sticks[0] + sticks[1]
#             sticks.append(sticks[0] + sticks[1])
#             sticks.pop(0)
#             sticks.pop(0)
            
#         return ans
        
        heapq.heapify(sticks)
        
        ans = 0
        
        while(len(sticks) > 1):
            cur = heapq.heappop(sticks) + heapq.heappop(sticks)
            ans += cur
            heapq.heappush(sticks, cur)
            
        return ans
