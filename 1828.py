# Queries on Number of Points Inside a Circle

import math

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = [0] * len(queries)
        
        for i in range(len(queries)):
            for j in range(len(points)):
                if (self.getDist(queries[i], points[j]) <= queries[i][2]):
                    ans[i] += 1
        return ans
        
        
        
    def getDist(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + 
                         (p1[1] - p2[1]) ** 2)
