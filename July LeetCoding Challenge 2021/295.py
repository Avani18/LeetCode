from sortedcontainers import SortedList

class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ar = SortedList()
        
    def addNum(self, num: int) -> None:
        self.ar.add(num)
        

    def findMedian(self) -> float:
        l = len(self.ar)
        med = 0
        if(l % 2 == 0):
            med = (self.ar[l//2] + self.ar[l//2 - 1])/2
        else:
            med = self.ar[l//2]
        return med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
