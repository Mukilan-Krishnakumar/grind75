from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # Left refers to the left pointer
        # Right referes to the right pointer
        left = 0
        right = 1
        max_profit = 0
        n = len(prices)
        while right < n:
            # we calculate profit as difference between price of right and left
            profit = prices[right] - prices[left]
            # if positive profit, we check if we have crossed max profit
            if prices[left] < prices[right]:
                max_profit = max(max_profit, profit)
            # Else, we update the left pointer to the position of right
            else:
                left = right
            # Every loop, we update right pointer to keep moving forward, or sliding forward
            right += 1
            
        return max_profit
