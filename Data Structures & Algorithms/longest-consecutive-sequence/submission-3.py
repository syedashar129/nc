class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        nums_set = set(nums)
        
        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                while num+1 in nums_set:
                    num+=1
                    length+=1
                longest = max(length, longest)
        return longest
    
# nums can be empty
# duplicates should be not be conisdered


# brute: nlogn / 1 --> sort and see by measuing the max or n^2 soliutiom to 
# optimal: 


# count tracker of max 
# make nums a set

# check start of sequnce (no n-1)
    # yes --> add to hashmap (start number, count) chekc if n+1 exists in nums set
    # no --> skip
# return longest

# n / n
