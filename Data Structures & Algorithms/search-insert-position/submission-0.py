class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = hi - lo // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else: # target == mid
                return mid
        return lo 


# distinct --> one result 
# sorted --> binary
# if not found --> return potential palce where it would be

# lo, hi
# while lo <= hi
#   mid 
#   if target < mid
#   elif target > mid 
#   else (target == mid)

# return lo

# time: O(logn)
# space: O(1)