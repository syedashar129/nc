class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sortedWord = sorted(word)
            anagram_map[tuple(sortedWord)].append(word)
        return list(anagram_map.values())
                


    

# any order
# same chars contians 

# group by map 
# sorted keys of letters (key), words (values)
# nlogk / n

# map
# loop strs
    # sort str
    # is sorted str in map?
        # yes --> add 
        # no --> add a new entry
# return values of map as array