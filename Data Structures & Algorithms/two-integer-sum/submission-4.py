class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_arr = []

        for index, number in enumerate(nums):
            target_num = target - number

            #does target_num exist in list?
            if target_num in nums:
                final_arr.append(index)
                final_arr.append(nums.index(target_num))
                return final_arr

            


        