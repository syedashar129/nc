class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target_map = defaultdict(int)

        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in target_map:
                return [target_map[diff], idx + 1]
            target_map[num] = idx + 1
        

# increasing order
# index1 < index and can not be equal 
# valid solution always 
# O(1) space
# 1 indexed --> starts at 1

# basically 2 sum but 1-indexed 

# brute: nested loop to look at all (n^2 / 1)
# optimal: hashmap ( n / 1)

# map 
# loop idx, num in nums:
    # diff = target - num 
    # if diff in map:
        # return [map[diff], idx + 1]
    # map[num] = idx + 1