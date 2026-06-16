class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow





# the brute force --> hashmap + count hte number times and if hte number of times is greater than 1 then dont count it
# time: o(n)
# space: O(n) --> o(1)

# 2 pointer --> reduce space
# increasing order
# fast and slow pointer

# slow = 0
# fast = 1
# loop
    #  if slowval != fastval:
    #     slow up 1
    #     slowval = fastval 
    # fast val up one

# return slowval index + 1



# time: O(n)
# space: O(1)


