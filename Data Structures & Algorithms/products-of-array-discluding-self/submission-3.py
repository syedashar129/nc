class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        running_prod_pre = 1
        for i in range(len(nums)):
            res[i] = running_prod_pre
            running_prod_pre *= nums[i]
        
        running_prod_post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= running_prod_post
            running_prod_post *= nums[i]
        
        return res
    

# each result index is the product of eveyrhting but itself
# avoid diviison 

# brute: n / 1 --> take sum of everything and divide the current number from it
# optimal: --> prefix and postfix

# prefix 
    # prefix_arr = []
    # prod = 1
    # loop nums
        # prefix_arr[index] = prod
        # prod *= nums[i]

# postfix 
    # postfix_arr  = []
    # prod = 1
    # reverse loop nums
        # prefixpostfix_arr[index] = prod
        # prod *= nums[i]
# return prefix vs postfix

# time: n
# space: n
