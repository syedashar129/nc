class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        min_element = float('inf')

        while lo <= hi:
            mid = (lo + hi) //2
            mid_num = nums[mid]

            if mid_num < min_element:
                min_element = mid_num
           
            if mid_num < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
    
        return min_element



        
# unique --no dupes
# ordered
# orderd between 1 and n times

# sort and then return the smallest element in list 

# brute force --> get min --> O(n)
# brute force --> sort and get first index --> o(n)
# binary serach --> search for smallest element

# lo = 0
# hi = len(nums) - 1
# min_element = 0

# while lo <= hi
    # mid
    # num 

    # if num > mid --> lo = mid + 1
    # elif num <= mid --> hi = mid - 1

# return min_element


# time: O(logn)
# space: O(1)