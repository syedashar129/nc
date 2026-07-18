class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        max_sub_len = 0 
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])

            max_sub_len = max(max_sub_len, r - l + 1)
        
        return max_sub_len


# sliding windwo w

# l = 0 
# max_sub_len = 0
# set 

# for r in s
    # while the right one is in the set 
        # remove the left one 
    
    # add the right one to the set 

    # max(maxsublen, r - l + 1)

# return maxsublen

# time: O(n)
# space: O(n) worst, avg of O(k)