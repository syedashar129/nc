class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)

        return set_s == set_t and (len(set_s) == len(set_t))
        #return set(s) == set(t) and 