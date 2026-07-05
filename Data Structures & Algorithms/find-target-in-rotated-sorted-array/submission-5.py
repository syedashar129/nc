class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min_index(nums)
        left_search = self.binary_search(nums, target, 0, min_index - 1)# left search 
        right_search = self.binary_search(nums, target, min_index, len(nums) - 1)# right search 

        if left_search == -1:
            return right_search
        else:
            return left_search


    def find_min_index(self,nums ):
        lo = 0 
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            mid_num = nums[mid]

            if mid_num < nums[hi]:
                hi = mid
            elif mid_num > nums[hi] :
                lo = mid + 1
            else:
                hi -= 1
        
        return lo
    
    def binary_search(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        
        return -1

    

#find min index 
# binary serach