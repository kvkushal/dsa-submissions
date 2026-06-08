class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        n=len(prices)
        r=1
        res=0

        while r<n:
            if prices[l]<prices[r]:
                res=max(res,prices[r]-prices[l])
            else:
                l=r
            r+=1

        return res