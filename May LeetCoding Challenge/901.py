# Online Stock Span
# https://leetcode.com/problems/online-stock-span/
'''Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].'''

class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
          
        weight = 1
        while (self.prices and self.prices[-1][0] <= price):
            weight += self.prices.pop()[1]
        self.prices.append((price, weight))
        return weight
        
obj1 = StockSpanner()
print (obj1.next(100))
print (obj1.next(80))
print (obj1.next(60))
print (obj1.next(70))
print (obj1.next(60))
print (obj1.next(75))
print (obj1.next(85))
