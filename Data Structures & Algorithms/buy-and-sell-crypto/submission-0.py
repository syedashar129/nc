class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[r] - prices[l] > max_profit:
                max_profit =  prices[r] - prices[l]
            
            if prices[r] <= prices[l]:
                l = r
        
            r += 1

        
        return max_profit


# sliding window 
    # start at first pointer. 
    # if number keesp going less --> make window bigger
    # if number less than or equia --> reset the pointer, record profit, compare with max

# time: O(n)
# space: O(1)
# 10,1,5,6,7,1, 10