# Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda a: (a[0], -a[1]))
        n = 0
        comp = -1
        for interval in intervals:
            if comp < interval[1]:
                n += 1
                comp = max(comp, interval[1])
                
        return n
                
