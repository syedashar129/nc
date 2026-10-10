class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


# anagrams = exact same charcaters (contain) w/diff order
    # length will be the same 
    # contain will be the same
# group all anagrams in ANY order

# return array of arrays

# brute force: n^2 / n --> bc 
# optimal: n / n --> hashmap w/key as the letters and then the words as the values
                    # iterate and add into the map
                    # cerate array of the values

# iterrate input:
    # check if curr mathes any key 
        # if yes --> add into that key as value
        # else --> add a new entry in the map (key/value)
    # return array of values


