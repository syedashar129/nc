class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. freq map 
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # 2. Create buckets(index = frequency, value = list of numbers)
        freq = [[] for i in range(len(nums) + 1)]

        # 3. Group  by freq
        for num, count in freq_map.items():
            freq[count].append(num)

        # 4. Iterate backwards to get top k (low --> high)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


# map
# iterate nums
    # if num in map:
        # append to that 
    # else
        # create new entry and add the word
# return top k values

# return any order
# return top k numbers in list

# brute force: n^2logn / n --> each index and then iterate to see the count and store in list sorted and hten take the top k from list
# optimal: n / n --> use hashmap (number : count), then take the top 2 counts and return the keys