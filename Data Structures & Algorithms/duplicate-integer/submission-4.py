class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    
# this is a set question 
# checking for existence

# set(nums) 

# brute force: nlogn / 1 sort and then check any past number and curr number == 
# optimal: n / n --> set and comapre length with input
    
# return len(set(nums)) != len(nums)