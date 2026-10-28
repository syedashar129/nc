class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i 
            leftSum += nums[i]
        return -1

    
# pivot = sum of all number left == index == sum of all numbers right
# if it is left most or right most index t--> 0 
# return leftmost ipivot index else -1 

# brute:
# optimal: 