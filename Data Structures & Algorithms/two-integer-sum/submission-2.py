class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):  # Use enumerate to get indices
            num2 = target - num1
            if num2 in nums:
                j = nums.index(num2)  # Find the index of num2
                if i != j:  # Check if indices are different
                    return [i, j]



        