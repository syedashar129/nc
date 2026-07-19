class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

    
# sliding window
# left and righ t
# check window size - max letter > k 



# l = 0 
# count = {}

# for r in s
    # append r count in count

    # while window size - max > k 
        # remove from letter count 
        # move ppointer up 1 

    # take max of res (window size)

# return res

# time: o(n)
# space: O(n)