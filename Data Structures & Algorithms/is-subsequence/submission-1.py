class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0 
        pointer_t = 0

        while pointer_s < len(s) and pointer_t < len(t):
            pointer_s_val = s[pointer_s]
            pointer_t_val = t[pointer_t]

            if pointer_s_val == pointer_t_val:
                pointer_s += 1
            pointer_t += 1
        
        return len(s) == pointer_s
            

# subsequence = in order letter
# s will be smaller than t --> 

# brute:
# optimal: n+m / 1 --> 2 pointer (one on s and one on t)


# pointer_s
# pointer_t 

# while t end
    # if pointer_s_val == poiner_t_val --> move up s pointer
    # move up t pointer 

# return pointer_s == len(s)