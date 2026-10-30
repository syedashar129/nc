class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0 

        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        return len(s) == pointer_s
    

# subssequence = deleteign some cahrs in some postions to get the next string
# s in t
# return boolean 


# brute:
# optimal: t / 1

# pointer s = 0
# poitner t = 0 

# while t 
    # if s[i] == t[i] --> increase s  
    # increase t poitners 

# return pointer s has reached above the end 