# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.'''


from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edge = defaultdict(list)
        for u, v, w in flights:
            edge[u].append((v, w))
        dist = {}
        q = [(0, src, 0)]
        while q:
            cost, cur, k = heapq.heappop(q)
            if k > K + 1 or cost > dist.get((cur, k), float('inf')):
                continue
            if cur == dst:
                return cost
            for node, w in edge[cur]:
                tmp = cost + w
                if tmp < dist.get((node, k + 1), float('inf')):
                    heapq.heappush(q, (tmp, node, k + 1))
                    dist[(node, k + 1)] = tmp
        return -1
