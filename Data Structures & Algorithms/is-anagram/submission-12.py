class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check len 
        if len(s) != len(t):
            return False
        st_map = defaultdict(int) # letter : count

        for c in s:
            st_map[c] += 1
            
        for c in t:
            st_map[c] -= 1
        
        for val in st_map.values():
            if val != 0:
                return False
        
        return True
        

    

# same characters, same # of times
# order does not matter (existence check) --> set? 

# brute: --> nlogn / 1 sort and comapre
# optinmal: nm / nm --> use a map (letter : count) and compare hashmaps equal or not

# check len checks --> n 
# make freq map of S --n / n 
# make fre1 map of T --? n / n
# check if size equal --> tru else false --> 1 