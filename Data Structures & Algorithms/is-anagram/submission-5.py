class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        print(f'sorted s : {sorted_s}')
        print(f'sorted t : {sorted_t}')

        for letter in s:
            if letter not in t:
                return False

        return True