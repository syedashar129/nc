class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        res = []

        for num in nums:
            freq_map[num] += 1
        
        freq_buckets = [[] for i in range(len(nums) + 1)]
        for num, count in freq_map.items():
            freq_buckets[count].append(num)
        
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
    

# answer unique --> means that wont be duplciate of same count 
# return in any order the top k 
# not sorted
# freq map? 

# brute:  nlogn / n --> hashmap (num : count). return the top k values from map. nlogn since we have to sort
# optimal: n / n --> hashmap + bucket sort


# freq map 
# for num in nums:
    # add to freq map (num : count)

# create buckeres (array)
# add to buckets (index = count, val = num with taht count) from the freq_map. this is getting entered sorted

# revrese the buckets nad grab the top k