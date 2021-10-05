# K Closest Points to Origin

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def keyy(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        points = sorted(points, key = keyy)
        
        return points[:k]
