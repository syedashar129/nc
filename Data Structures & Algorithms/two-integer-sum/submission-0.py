class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in nums:
            if (target - number) in nums:
                number_2 = target - number
                num1_index = nums.index(number)
                num2_index = nums.index(number_2)

                return [num1_index, num2_index]



        