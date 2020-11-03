# Kids With the Greatest Number of Candies


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxc = max(candies)
        for i in candies:
            if (i + extraCandies) >= maxc:
                ans.append(True)
            else:
                ans.append(False)
        return ans
