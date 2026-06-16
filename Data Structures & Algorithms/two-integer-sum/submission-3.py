class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indexes which add up to the target

        saved_first_num = 0
        for number in nums:
            target_num = target - number

            #does target_num exist in list?

        