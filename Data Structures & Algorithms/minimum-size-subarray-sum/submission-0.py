class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        total = 0
        res = float("inf") # min sliding window size

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return res if res != float("inf") else 0





# sliding window 

# l 
# total (compare with target)
# res --> most min window size

#  iterate with r across nums 
    # add r to total
    # while total is greater than or equal to target 
        # record res
        # decrement the l amount from total 
        # inncrement l pointer

# return res if res != float else 0 


# time: O(n)
# space: O(1)
