class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if c1 in mapST and mapST[c1] != c2 or c2 in mapTS and mapTS[c2] != c1:
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True
    
# isomorphic = if s can be replaced to get t 
# order same 

# brute: 
# optimal:

# 2 maps
# iterate s 
    # if s --> t or t --> s    --> return false
    # add in both maps 

# return true

# n / n 