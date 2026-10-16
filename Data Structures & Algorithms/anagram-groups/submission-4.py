class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
    


# return in any order 
# anagram --> exact same characters in diff order (contains)

# brute force: nlogk / n --> store sorted words as keys, and then append the follwing words
# optimal: n*k / n*k -->  key as a binary list

# loop strings 
    # loop chars in strings 
        # convert the string to binary
        # make key as binary : string
    # return the values as a list 
