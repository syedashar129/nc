class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1: find intersecrion / cycle existence
        slow = 0 
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: # we found a cycle
                break

        # 2: Find extrance of cycle (dupe)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        

        



    
# 1 extra int 
# range of 1 --> N 
# exactly one repeated 
# return repeated int




