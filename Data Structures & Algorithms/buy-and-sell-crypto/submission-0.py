class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        minprice = float('inf')
        maxprice = 0

        for i in range(n):
            minprice = min(minprice,prices[i])
            maxprice = max(maxprice, prices[i]-minprice)

        return maxprice
        