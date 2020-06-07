# Coin Change 2
# https://leetcode.com/problems/coin-change-2/
'''You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.'''

def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def rec(amt, index):
            if amt == 0:
                return 1
            if amt<0 or index==n:
                return 0
           
            curr_res = 0

            for i, coin in enumerate(coins[index:], index):
                curr_res += rec(amt-coin, i)
            return curr_res

        coins.sort(reverse=True)
        return rec(amount, 0)
