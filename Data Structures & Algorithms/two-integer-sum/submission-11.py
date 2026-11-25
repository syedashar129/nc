class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = defaultdict(int)

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in target_map:
                return [target_map[diff], idx]
            target_map[num] = idx


# i != j 
# one exact pair 
# return smaller index first 

# brute: loop nested to get all until target found (n^2, 1)
# optimal: hashmap to store and check in map n / n

# map
# loop num in nums 
    # diff = target - num 
    # if diff in map:
        # return [map[diff], curr_idx]
    # add num to map w idx
