class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            # if found --> return 
            if nums[i] in window:
                return True 
            
            # if not found --> extend window 
            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])
        
        return False
                


# 1. vallues are teh same --> duplicates 
# 2. which are k steps away 

# sliding window --> fixed window size of k 

# 0 -> 3 
# if found --> return true 
# if not found --. extend window and check again UNTIL reach end

# start pointer = 0 
# end pointer = k

# while end pointer <= end
    # if found --> return true 
    # if not found --> extend window

# return False

