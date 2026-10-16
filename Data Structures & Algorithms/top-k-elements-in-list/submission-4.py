class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        res = []

        for num in nums:
            freq_map[num] += 1 # 1 : 1, 2 : 2, 3 : 3
        
        buckets = [[] for i in range(len(nums) + 1)] # [[], [1], [2], [3]] 7

        for n, c in freq_map.items():
            buckets[c].append(n) # [[], [1], [2], [3]] 7
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


# always unique
# any order

# brute force: nlogn / n --> hashmap (number : count) --> sort the values and grab the top k values
# optimal: n / n --> hashmap (number : count) --> put numbrs into buckets (by index) --> reverse order and grab top k

# == bucket sort

# hashmap 
# loop nums
    #  number : count 

# final = array of arrays

# index in hashmap.items() (already sorted least freq --> most freq)
    # at index place value [[], [2], [3, 4]]

# revrese the final array and stop once we have k numbers