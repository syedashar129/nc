class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_val_map = {}
        for index, num in enumerate(nums):
            first_val = target - num
            if first_val in existing_val_map:
                return [existing_val_map[first_val], index] # 0: 2
            else:
                existing_val_map[num] = index # 4 : 0, 5 : 1, 

# 4 5 6 --- 10 
            
        
# cant use the same index 
# return smallest index first 
# must have a result

# brute force: n^2 time ? 
# using a hashmap 
    # is target - curr_val in hashmap
        # if yes --> return [index of taregt - curr_val, curr_index]
        # else --> do nothing and store in the hashmap and iterate to next index

# time: O(n)
# space: O(n) ? --> bc we are storin all elements in hashmap at worst case


    