from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                profit_list.append(prices[j] - prices[i])
        profit_list = sorted(profit_list)
        if len(profit_list) == 0:
            return 0
        else:
            profit = profit_list[-1]
            if profit < 0:
                profit = 0
            return profit

s = Solution()
resp = s.maxProfit([7,1,5,6,3])
print(resp)
