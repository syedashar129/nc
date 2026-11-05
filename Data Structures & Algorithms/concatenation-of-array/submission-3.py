class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        final_arr = []

        # 1st pass
        for num in nums:
            final_arr.append(num)
        
        # 2nd pass
        for num in nums:
            final_arr.append(num)

        return final_arr



# store the length 
# 2 pass
#   1. build the first array using just whats there --. O(n)
#   2. build the second array in second pass --. O(n)


# time: o(n)
# space: O(2n) --> O(n)


