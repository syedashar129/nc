class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check len 
        if len(s) != len(t):
            return False
        s_map = defaultdict(int) # letter : count
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1
            
        for c in t:
            t_map[c] += 1
        
        return s_map == t_map
        

    

# same characters, same # of times
# order does not matter (existence check) --> set? 

# brute: --> nlogn / 1 sort and comapre
# optinmal: nm / nm --> use a map (letter : count) and compare hashmaps equal or not

# check len checks --> n 
# make freq map of S --n / n 
# make fre1 map of T --? n / n
# check if size equal --> tru else false --> 1 