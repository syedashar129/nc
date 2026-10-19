class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #  Initializes the object given an integer k and the stream of integers nums.
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # Adds the integer val to the stream and returns the kth largest integer in the stream.
        # push 
        heapq.heappush(self.minheap, val)
        # remove until k 
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        # return min
        return self.minheap[0]


# not sorted
# incldue duplicates


        
