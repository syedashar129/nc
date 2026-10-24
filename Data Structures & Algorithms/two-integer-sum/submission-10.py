class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_index_map:
                return [num_index_map[diff], index]
            else:
                num_index_map[num] = index

    

    
# unique solution --> no duplicate
# cant use the same index --> keep moving on 
# smallest index first (one in map, curr)
# always a solution

# brute: n^2 / 1 --> nested loop to go through each one until target pair is found 
# optimal: n / n --> hashmap (num : index). using teh num as the key here as we ned existence check in the map 

# map 
# loop num in nums
    # does target - currNum exist in map
        # yes --> return indices [curr index, map index]
        # no --> add {num : index}

