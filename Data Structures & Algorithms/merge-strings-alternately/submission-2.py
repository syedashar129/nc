class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # go through both inputs
        word1p = 0
        res = []
        while word1p <= len(word1) - 1 and word1p <= len(word2) - 1:
            res.append(word1[word1p])
            res.append(word2[word1p])
            word1p+=1

        # leftovers
        res.append(word1[word1p:])
        res.append(word2[word1p:])

        # return new string
        return ''.join(res)

# 2 pointer 
# time: O(n + m)
# space: O(n + m)