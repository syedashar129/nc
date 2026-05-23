class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 poiners
        left, right = 0, len(nums) - 1
        i = 0

        def swap(x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp

        while i <= right:
            if nums[i] == 0:
                swap(left, i) # swap to the left
                left += 1 
            elif nums[i] == 2:
                swap(right, i)# swap to the right
                right -= 1
                i -= 1
            i += 1


# 1 pass = dutch flag algo

# time: O(n)
# space: O(1)

        