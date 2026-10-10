class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        sortedmap = sorted(freq_map, key=freq_map.get, reverse=True)
        return sortedmap[:k]


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