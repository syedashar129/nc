class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums) - 1

        while lo <= hi:
            mid = hi - lo // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid
        
        return -1 


# binary search question 
# sorted

# lo and hi --> indexes
# while low <= hi
#   mid
#   if target > mid --> low = mid + 1
#   if taget < mid  --> hi = mid - 1
#   if target == mid --> return mid

# return -1 


# time: O(nlogn)
# space: O(1)