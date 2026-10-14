class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # put into count map 
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # put into the freq bucket 
        for n, c in count.items():
            freq[c].append(n)
        
        # reverse and get the k count numbers 
        for bucket_index in range(len(freq) - 1, 0, -1):
            for num in freq[bucket_index]:
                res.append(num)
                if len(res) == k:
                    return res


# any order
# one answer 


# brute force: 
    # 1. hashmap --> nlogn / n store all elements to a hashmap (number : count) --> sort the values by count and grab teh top k 
# optimal: bucket sort --> n / n --> 
    # map : (count : number)
    # we go backwards and grab the top k numbers 
    # return


# {} --> count : number
# [] --> [[], [], [], ...]
# last k 

# make the map (number : count)
# put into the bucket
# reverse the bucket 
