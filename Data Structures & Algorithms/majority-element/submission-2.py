class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_majority_num, count = 0, 0

        for num in nums:
            if count == 0:
                curr_majority_num = num
        
            count += (1 if curr_majority_num == num else -1)
        
        return curr_majority_num
    




# goal O(n) n O(1)
# time; o(n)
# space: O(1)
