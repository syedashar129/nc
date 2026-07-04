class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min_index(nums)
        left_result = self.binary_search(nums, target, 0, min_index - 1)
        right_result = self.binary_search(nums, target, min_index, len(nums) - 1)

        if left_result == -1:
            return right_result
        else:
            return left_result

    def find_min_index(self, nums):
        lo = 0 
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return lo

    def binary_search(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
            

        return -1





# find min 
# search left 
# search right

# if not in left --> return right 
# else -- return left
# search using binary seearch based on hi since there is cliffs and rotated 
# if found return num 


# binary search sol 
# lo = 0 
# hi = len(nums) - 1

# while lo <= hi
    # mid 
    # mid_num 

    # if mid_num == target:
        # return mid_num 
    
    # if mid num > hi --> lower
    # if mid num < hi --> higher

# return -1 

# time: O(logn)
# space: O(1)