# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
'''We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)'''


def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            heappush(pq, ((x**2 + y**2, x, y)))
        
        res = []
        for i in range(K):
            _, x, y = heappop(pq)
            res.append([x, y])
        return res
