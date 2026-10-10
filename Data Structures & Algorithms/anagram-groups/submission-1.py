class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in anagram_map:
                # add into exisitng value 
                anagram_map[key].append(word)
            else:
                # add new key/value
                anagram_map[key] = [word]
        return list(anagram_map.values())


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


