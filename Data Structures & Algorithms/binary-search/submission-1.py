class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0  # first idx
        hi = len(nums) - 1 # last idx
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = nums[mid]
            if target > mid_value:
                lo = mid + 1
            elif target < mid_value:
                hi = mid - 1
            else:
                return mid
        return -1 
    

# distinct integers (unique)
# sorted 
# if exists --> return index
# if not exists --> return -1 

# brute: n / 1 --> go throgh array and find when taregt == current number
# optimal: logn / 1 --> binary search 

# while lo <= hi
    # mid = (lo + hi) // 2
    # if target > mid --> lo = mid + 1
    # if target < mid --> hi = mid - 1
    # if target == mid --> return index

# return -1 

