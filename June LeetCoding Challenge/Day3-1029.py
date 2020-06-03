# Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/
'''There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.'''


def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1]-x[0])
        total = 0
        for i in range(len(costs)//2):
            total += costs[i][1]
        for i in range(len(costs)//2, len(costs)):
            total += costs[i][0]
        return total
