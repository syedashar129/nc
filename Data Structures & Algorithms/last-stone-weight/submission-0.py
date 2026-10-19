class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # largest negative (-6)
            second = heapq.heappop(stones) # second largest negative (-4)

            if first < second:
                heapq.heappush(stones, first - second)
        
        heapq.heappush(stones, 0) # if heap empty in end
        return abs(stones[0])




# make all negative and use mnin heap 

        # while minheap > 1
            # first = heap.pop
            # second = heap.pop
            # if second > first
                # add left over to heap

        # append 0 --> if emptt 
        # grab abs(min) --> leftover value

    
