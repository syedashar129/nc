class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #(chars as literal chars binary : list of words)

        for word in strs:
            binary = [0] * 26
            for c in word:
                c_in = ord(c) - ord('a')
                binary[c_in] += 1
            anagram_map[tuple(binary)].append(word)
        
        return list(anagram_map.values())

    
# same chars, same # , order can be diff --> map freq
# return in any order

# brute: n^2 / n --> loop thorugh each one and check if anagram and add it
# optimal: nm / nm --> hashmap (chars as literal chars binary : word)

# another: nmlogn / nm --> map : sort each word and store it in key and then sort and add word to the val

# map
# loop word in strs:
    # binary = cretae binary of word
    # check if binary in map
        # yes --> append to that key 
        # no --> create new par
   # return all values as a list of lists


