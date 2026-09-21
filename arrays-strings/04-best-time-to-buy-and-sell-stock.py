class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for price in prices[1:]:
            profit=price-min_price
            max_profit=max(max_profit,profit)
            min_price=min(price,min_price)
        return max_profit

prices=list(map(int,input().split()))
res=Solution().maxProfit(prices)
print(res)