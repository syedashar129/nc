class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]
        
        return profit 
    

# greedy
# time: O(n)
# space: O(1) --> profit

# up trend 
# core: current price > last price --> current price - last price and add to profit

# 4 + 3 = 7