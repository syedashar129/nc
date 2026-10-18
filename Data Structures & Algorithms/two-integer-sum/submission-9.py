class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            first_num = target - num
            if first_num in nums_map:
                return [nums_map[first_num], idx]
            nums_map[num] = idx
            



    
# diff indexes 
# every one has a pair 
# return (small index, larger index)

# brute: n^2 / 1 
# optimal:  n / n --> map (value : index)

# map 
# loop index, num in nums
    # if target - num in map:
        # return [map.get(target - num), index]
    # insert into map (num, index)
