class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        left_idx = self.findLeftMostTargetIndex(nums, lo, hi, target)
        if left_idx == -1:
            return [-1, -1]
        right_idx = self.findRightMostTargetIndex(nums, lo, hi, target)
        return [left_idx, right_idx]

    
    def findLeftMostTargetIndex(self, nums, lo, hi, target):
        left_most_idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = nums[mid]
            if target < mid_value:
                hi = mid - 1
            elif target > mid_value:
                lo = mid + 1
            else:
                left_most_idx = mid
                hi = mid - 1
        return left_most_idx
        

    def findRightMostTargetIndex(self, nums, lo, hi, target):
        right_most_idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = nums[mid]
            if target < mid_value:
                hi = mid - 1
            elif target > mid_value:
                lo = mid + 1
            else:
                right_most_idx = mid
                lo = mid + 1
        return  right_most_idx

# sorted 
# if target found --> return start and end 
# if target not found --> return [-1, 1]
# consecutive

# binarys search 

# brute: n / 1 --> find target and then check until the target ends (start, end)
# optimal: logn / 1 --> binary search 


# left bound scan --> left most target indedx (search1)
# if left is -1
    # return [-1, -1]
# right bound scan--> right most target indedx (search2)
# return [left_idx, right_idx]


